import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    # directory - relative path within - working_directory
    # LLM specifies which directory it wants to scan
    # working_directory will be set by us
    try:
        #1. Check to see if directory is in working_directory
        abs_working_dir = os.path.abspath(working_directory)
        # print(working_dir_abs)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        # print(target_dir)

        #2. Check if target_dir falls within absolute working_directory
        # Will be True or False
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        return f"Error: {e}"

