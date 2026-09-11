import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_path,directory))
        if os.path.commonpath([working_path, target_dir]) != working_path:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if os.path.isdir(target_dir):
            dir_list = os.listdir(target_dir)
            contents_lines = []
            for item in dir_list:
                item_path = os.path.join(target_dir, item)
                new_line = f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
                contents_lines.append(new_line)
            return ("\n".join(contents_lines))
        else:
            return (f'Error: "{directory}" is not a directory')
    except Exception as e: #noqa
        return f"Error: {e}"
