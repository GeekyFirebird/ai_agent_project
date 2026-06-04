import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    # directory - relative path within - working_directory
    # LLM specifies which directory it wants to scan
    # working_directory will be set by us
    try:
        #1. Check to see if directory is in working_directory
        working_dir_abs = os.path.abspath(working_directory)
        # print(working_dir_abs)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # print(target_dir)

        if os.path.isdir(directory):
            print(f'Success: "{directory}" is within the working directory')
        else:
            print(f'Error: "{directory}" is not a directory')

        #2. Check if target_dir falls within absolute working_directory
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"

