# main.py
import os
from organizer.config import DEFAULT_SOURCE_FOLDER
from organizer.scanner import scan_directory
from organizer.sorter import get_category
from organizer.mover import move_file

def main():
    target_dir = input(f"Enter folder path to organize (Press Enter for default: {DEFAULT_SOURCE_FOLDER}): ")
    
    if not target_dir:
        target_dir = DEFAULT_SOURCE_FOLDER

    if not os.path.exists(target_dir):
        print("Invalid path provided.")
        return

    print(f"--> Scanning: {target_dir}...")
    
    files = scan_directory(target_dir)
    
    if not files:
        print("No files found to organize!")
        return

    print(f"--> Found {len(files)} files. Organizing now...\n")

    for file in files:
        # 1. Identify Category
        category = get_category(file)
        
        # 2. Move File
        move_file(file, category, target_dir)

    print("\n--> Organization Complete! ✅")

if __name__ == "__main__":
    main()