import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_path = os.path.abspath(working_directory)
        file_path_absolute = os.path.normpath(os.path.join(working_path,file_path))
        if os.path.commonpath([working_path,file_path_absolute]) != working_path:
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(file_path_absolute):
            return (f'Error: Cannot write to "{file_path}" as it is a directory')
        os.makedirs(os.path.dirname(file_path_absolute), exist_ok=True)
        with open(file_path_absolute, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: #noqa
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write to a file in the specified directory",
        "parameters": {
            "required": ["file_path" , "content"],
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Text to add to the file"

                },
            },
        },
    },
}
