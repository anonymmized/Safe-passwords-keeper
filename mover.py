import shutil

def mover_to_drive(drive, file_path):
    try:
        shutil.move(file_path, f'/Volumes/{drive}/{file_path}')
        print(f"[*] {file_path} moved to drive {drive} successfully.")
    except FileNotFoundError as err:
        print(f"Error moving {file_path}: {err}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")


def mover_from_drive(drive, file_path):
    try:
        shutil.move(f'/Volumes/{drive}/{file_path}', './returned_files')
        print(f"[*] {file_path} moved from drive {drive} successfully.")
    except FileNotFoundError as err:
        print(f"Error moving {file_path}: {err}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")