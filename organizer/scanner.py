# organizer/scanner.py
import os

def scan_directory(path):
    """
    Scans the directory and returns ONLY files (ignoring folders).
    """
    files = []
    try:
        # Check if path exists
        if not os.path.exists(path):
            print(f"❌ Directory not found: {path}")
            return []

        for entry in os.scandir(path):
            # STRICT CHECK: Only process files, ignore folders
            if entry.is_file():
                files.append(entry.name)
                
    except PermissionError:
        print(f"❌ Permission Denied for {path}")
    except Exception as e:
        print(f"❌ Error scanning directory: {e}")
        
    return files