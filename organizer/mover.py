# organizer/mover.py
import os
import shutil

def make_unique_filename(destination_folder, filename):
    """
    If file exists, appends a number (e.g., file_1.txt).
    Returns a unique filename.
    """
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    
    # Check if file exists, if yes, keep adding numbers until unique
    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1
        
    return new_filename

def move_file(filename, category, source_path):
    """
    Moves a single file to its corresponding category folder safely.
    """
    source_file = os.path.join(source_path, filename)
    destination_folder = os.path.join(source_path, category)
    
    # 1. Create the folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # 2. Handle Duplicates (The "Resume-Grade" Logic)
    unique_filename = make_unique_filename(destination_folder, filename)
    destination_file = os.path.join(destination_folder, unique_filename)

    # 3. Move
    try:
        shutil.move(source_file, destination_file)
        if filename != unique_filename:
            print(f"⚠️  Duplicate found! Renamed & Moved: {filename} -> {category}/{unique_filename}")
        else:
            print(f"✅ Moved: {filename} -> {category}/")
    except Exception as e:
        print(f"❌ Error moving {filename}: {e}")