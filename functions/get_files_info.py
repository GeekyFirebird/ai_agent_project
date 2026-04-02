import os

def get_files_info(working_directory, directory="."):
    #directory - relative path
    #The directory parameter can be specified by the LLM agent but the working_dir is set by us
    try:
        #Check if path to directory is inside working_directory
        working_dir_abs = os.path.abspath(working_directory)
        #os.path.abspath() get the absolute path of the working directory
            #absolute path - Full path starting at root

        #Construct the full path of the target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        #os.path.normpath - Normalize a pathname by collapsing redundant separators and up-level references so that A//B, A/B/, A/./B and A/foo/../B all become A/B

        #Check if target_dir falls within absolute working_directory path
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        #The common path should be the same as the working_dir_abs
        
        #if the directory is not a directory
        if not os.path.isdir(target_dir):
            f'Error: "{directory}" is not a directory'

        #Iterate over items in the target_dir
        #For each item record the name, file size, if its a dir
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)

    #Turn into a try/except to catch errors
    except Exception as e:
        return f"Error listing files: {e}"