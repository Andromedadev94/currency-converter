from pathlib import Path
from datetime import datetime
import shutil
time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
back_up_folder_name = f"backup_{time}"
back_up_folder_name_path = Path.home() / "Desktop" / back_up_folder_name
def backup_folder(folder_path):
    try:
        shutil.copytree(folder_path, back_up_folder_name_path, dirs_exist_ok=True)
        print(f"Folder '{folder_path}' has been backed up to '{back_up_folder_name_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")
# new_path = Path.home() / "Desktop" / "dll"
# backup_folder(new_path)
