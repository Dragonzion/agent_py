import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_path,directory))
        if os.path.commonpath([working_path, target_dir]) != working_path:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if os.path.isdir(target_dir):
            return (f'Success: "{directory}" is within the working directory')
        else:
            return (f'Error: "{directory}" is not a directory')
    except Exception as e: #noqa
        return f"Error: {e}"
