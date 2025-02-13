"""/Volumes/pass_keeper"""
import os


def mover(drive, filepath):        # <- сюда будет передаваться уже зашифрованный файл
    cur_dir = "/Volumes"
    folder_path = os.path.join(cur_dir, drive)
    os.system(f"mv {filepath} {folder_path}")

drive = input("[?] Enter the name of the drive: ")
filename = input("[?] Enter filename: ")
print("[*] Moving your file on flash drive...")
mover(drive, filename)
print("[***] Complete!")
