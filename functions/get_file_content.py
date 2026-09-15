import os

MAX_CHARS = 10000


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_path = os.path.abspath(working_directory)
        file_path_absolute = os.path.normpath(os.path.join(working_path,file_path))
        if os.path.commonpath([working_path,file_path_absolute]) != working_path:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if os.path.isfile(file_path_absolute) == False:
            return (f'Error: File not found or is not a regular file: "{file_path}"')
        with open(file_path_absolute, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e: #noqa
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "get content relative to the working directory",
        "parameters": {
            "required": ["file_path"],
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
