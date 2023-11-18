import os
import glob
import shutil

def rm_dir(path, pattern):
    """Remove the folder in a path, that matches the pattern"""
    # List all directories matching the pattern
    dir_pattern = os.path.join(path, pattern)
    directories = [d for d in glob.glob(dir_pattern) if os.path.isdir(d)]

    # Remove the directories
    for dir_path in directories:
        try:
            # If you are sure that directories are empty or you want to delete non-empty directories
            shutil.rmtree(dir_path)
            print(f"Removed old directory: {dir_path}")
        except OSError as e:
            print(f"Error: {e} - {dir_path}")