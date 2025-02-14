"""/Volumes/pass_keeper"""
import os

def mover(drive, filepath):        # <- сюда будет передаваться уже зашифрованный файл
    cur_dir = "/Volumes"
    folder_path = os.path.join(cur_dir, drive)
    os.system(f"mv {filepath} {folder_path}")
while True:
    drive = input("[?] Enter the name of the drive: ")
    if os.path.ismount(f"/Volumes/{drive}"):
        while True:
            filename = input("[?] Enter filename: ")
            if os.path.isfile(filename):
                print("[*] Moving your file on flash drive...")
                mover(drive, filename)
                print("[***] Complete!")
                break
            else:
                print("[!] There is no file like that, please retype...")
        break
    else:
        print("[!] There is no drive like that, please retype...")