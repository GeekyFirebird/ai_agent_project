import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Run a python file in a specified directory relative to the working directory",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="A file path to run a python file from, relative to the working directory",
                ),
            },
            required=["file_path"],
        ),
    )

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
      
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not abs_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]
        if args:
            command.extend(args)

        result = subprocess.run(
            command, 
            cwd=abs_working_dir,
            capture_output=True, 
            text=True, 
            timeout=30.0
        )

        output: list[str] = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        elif not result.stderr and not result.stdout:
            output.append("No output produced")
        else:
            output.append(f"STDOUT: {result.stdout} STDERR: {result.stderr}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"