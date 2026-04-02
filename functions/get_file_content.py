import os

def get_file_content(working_directory, file_path):
    try:
         working_dir_abs = os.path.abspath(working_directory)
         target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

         if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
         
         if not os.path.isfile(target_dir):
            f'Error: File not found or is not a regular file: "{file_path}"'