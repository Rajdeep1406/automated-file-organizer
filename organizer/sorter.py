import os
from .config import EXTENSION_MAP

def get_category(filename):
    """
    Determines the category of a file based on its extension.
    Returns 'Others' if no match is found.
    """
    # Get the file extension (e.g., '.jpg')
    _, extension = os.path.splitext(filename)
    extension = extension.lower()

    for category, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return category
            
    return "Others"  # Fallback folder