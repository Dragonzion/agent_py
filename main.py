import argparse
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionMessageToolCall

from call_function import available_functions
from functions.call_function import call_function
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("Missing API Key")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():
    print("Hello from agent-py!")

    # Gets user input
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    #Verbose optional
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages: list[ChatCompletionMessageParam] =[
        {
            "role": "system",
            "content": system_prompt
        },

        {
            "role": "user",
            "content": args.user_prompt ,
        }
    ]


    for _ in range(20):

        response = client.chat.completions.create(
            model="openrouter/free",
            messages = messages,
            tools = available_functions,
        )
        if response.usage == None:
            raise RuntimeError("response.usage is None")
        if args.verbose and _ ==0:
            print(f"User prompt: {args.user_prompt}")
        if args.verbose:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")


        message = response.choices[0].message
        messages.append(message.model_dump())  # type: ignore

        if message.tool_calls == None:
            print(message.content)
            break
        else:
            for tool_call in message.tool_calls:
                if isinstance(tool_call, ChatCompletionMessageToolCall):
                    result_message = call_function(tool_call, args.verbose)
                    messages.append(result_message)  # type: ignore
                    if args.verbose:
                        print(f"-> {result_message['content']}")
    else:
        print("Maximum number of messages reached")
        sys.exit(1)



if __name__ == "__main__":
    main()
