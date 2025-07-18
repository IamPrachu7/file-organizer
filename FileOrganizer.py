import os
import shutil
import logging
from typing import Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def create_folder_if_not_exists(path: str) -> None:
    """Create a folder if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def move_file_to_folder(src_path: str, dest_folder: str) -> None:
    """Move a file to the destination folder."""
    try:
        filename = os.path.basename(src_path)
        dest_path = os.path.join(dest_folder, filename)
        shutil.move(src_path, dest_path)
        logging.info(f"Moved '{filename}' to '{dest_folder}'")
    except (shutil.Error, OSError) as e:
        logging.error(f"Failed to move '{src_path}' to '{dest_folder}': {e}")

def organize_files(directory: str, extension_map: Dict[str, str]) -> None:
    """Organize files in a directory based on their extensions."""
    logging.info(f"Organizing files in: {directory}")

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            continue

        ext = os.path.splitext(item)[1][1:].lower()

        if ext in extension_map:
            folder_name = extension_map[ext]
            folder_path = os.path.join(directory, folder_name)
            create_folder_if_not_exists(folder_path)
            move_file_to_folder(item_path, folder_path)
        else:
            logging.info(f"Skipped '{item}': Unknown file type")

    logging.info("✅ File organization completed.")

def get_valid_directory() -> str:
    """
    Prompt user for a valid directory path.
    If blank, exit the program.
    """
    while True:
        user_input = input("Enter folder path to organize (or press Enter to cancel): ").strip()

        if user_input == "":
            print("⚠️ No path provided. File organization cancelled.")
            return None
        elif os.path.isdir(user_input):
            return user_input
        else:
            print("❌ Invalid folder path! Please try again.")

def main() -> None:
    """Main function to organize files based on their extensions."""
    file_extensions = {
        'pdf': 'PDFs', 'png': 'Images', 'jpg': 'Images', 'jpeg': 'Images',
        'gif': 'Images', 'svg': 'Images', 'webp': 'Images', 'heic': 'Images',
        'psd': 'Images', 'ai': 'Images', 'doc': 'Documents', 'docx': 'Documents',
        'txt': 'Documents', 'md': 'Documents', 'ppt': 'Documents', 'pptx': 'Documents',
        'csv': 'Data', 'xlsx': 'Data', 'xls': 'Data', 'json': 'Data', 'xml': 'Data',
        'zip': 'Archives', 'rar': 'Archives', '7z': 'Archives', 'tar': 'Archives',
        'gz': 'Archives', 'iso': 'Archives', 'pka': 'Archives', 'exe': 'Executables',
        'dll': 'Executables', 'mp3': 'Music', 'wav': 'Music', 'ogg': 'Music',
        'flac': 'Music', 'm4a': 'Music', 'mp4': 'Videos', 'avi': 'Videos',
        'flv': 'Videos', 'wmv': 'Videos', 'mkv': 'Videos', 'mov': 'Videos',
        'py': 'Scripts', 'pyc': 'Scripts', 'bat': 'Scripts', 'sh': 'Scripts',
        'js': 'Web', 'css': 'Web', 'html': 'Web'
    }

    target_directory = get_valid_directory()
    if target_directory:
        organize_files(target_directory, file_extensions)

if __name__ == "__main__":
    main()


