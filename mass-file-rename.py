from pathlib import Path
import os
def mass_rename():
    directory = Path.home() /"Desktop" /"dll"
    new_file_number = 1
    new_folder_number = 1
    if directory.exists():
        for file in directory.iterdir():
            if file.is_file():
                while (file.parent / f"file_{new_file_number}{file.suffix}").exists():
                    new_file_number += 1
                new_name = f"file_{new_file_number}{file.suffix}"
                try:
                    os.rename(file, file.parent / new_name)
                    print(f"{file.name} changed to {new_name}")
                except OSError as e:
                    print(f"Error renaming {file.name}: {e}")
            elif file.is_dir():
                while(file.parent / f"directory_{new_folder_number}").exists():
                    new_folder_number += 1
                new_folder_name = f"directory_{new_folder_number}"
                try:
                    os.rename(file, file.parent / new_folder_name)
                    print(f"Directory: {file.name} changed to {new_folder_name}")
                except OSError as e:
                    print(f"Error renaming directory {file.name}: {e}")
            else:
                print(f"Other: {file.name}")