from pathlib import Path
import shutil
folder_path = Path.home() / "Desktop" / "dll"
new_folders = ["Pictures" , "Documents", "Python"]
for folder in new_folders:
    new_path = folder_path / folder
    new_path.mkdir(exist_ok=True)

sub_folder_dic = {
    ".jpg" : folder_path / "Pictures",
    ".txt" : folder_path / "Documents",
    ".py" : folder_path / "Python"
}

for files in folder_path.iterdir():
    if files.is_file() and files.suffix.lower() in sub_folder_dic:
        print(files)
        shutil.move(files, sub_folder_dic[files.suffix])
