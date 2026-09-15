import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:

        working_path = os.path.abspath(working_directory)
        file_path_absolute = os.path.normpath(os.path.join(working_path,file_path))
        if os.path.commonpath([working_path,file_path_absolute]) != working_path:
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(file_path_absolute):
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        if file_path.endswith(".py") == False:
            return (f'Error: "{file_path}" is not a Python file')
        command = ["python", file_path_absolute]
        if args != None:
            command.extend(args)
        comp_process = subprocess.run(command, cwd=working_path, capture_output=True, text=True, timeout=30)#noqa
        output = []
        if comp_process.returncode != 0:
            output.append(f"Process exited with code {comp_process.returncode}")
        if not comp_process.stdout and not comp_process.stderr:
            output.append("No output produced")
        else:
            if comp_process.stdout:
                output.append(f"STDOUT:\n{comp_process.stdout}")
            if comp_process.stderr:
                output.append(f"STDERR:\n{comp_process.stderr}")
        return "\n".join(output)
    except Exception as e: #noqa
        return f"Error: executing Python file: {e}"
