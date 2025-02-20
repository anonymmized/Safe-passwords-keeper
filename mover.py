import shutil
import os

def mover_to_drive(drive, filename, source_directory):
    if filename.startswith("._"):
        print(f"[!] Skipping hidden file: {filename}")
        return

    source_path = os.path.join(source_directory, filename)
    destination_path = os.path.join(f"/Volumes/{drive}", filename)

    try:
        shutil.move(source_path, destination_path)
        print(f"[+] Moved {filename} to {destination_path}")

        # Удаление скрытых файлов (если они существуют)
        hidden_file = f"._{filename}"
        hidden_file_path = os.path.join(destination_path, hidden_file)
        if os.path.exists(hidden_file_path):
            os.remove(hidden_file_path)
            print(f"[+] Removed hidden file: {hidden_file}")

    except Exception as e:
        print(f"[!] Error moving {filename}: {e}")

def mover_from_drive(drive, file_path, to_path):
    """Moves a file from a specified drive to a specified path."""
    try:
        # Перемещаем файл с флешки в локальную директорию
        shutil.move(f'/Volumes/{drive}/{file_path}', to_path)
        print(f"[*] {file_path} moved from drive {drive} successfully.")
    except FileNotFoundError as err:
        print(f"Error moving {file_path}: {err}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")