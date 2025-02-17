"""
import mover"""
import os
from encode_file import encrypt_file
from decode_file import decrypt_file
from cryptography.fernet import Fernet
from mover import mover
import time

def main():
    print("[#] This program moving your files with 'pass' in filenames to flash drive!")
    time.sleep(3)
    answ = input("[*] Preparation is completed\n Do you want to move your files [Y/n]: ")
    while True:
        if answ == "y" or answ == "Y":
            answer_to_encode = input("[!] Now program is ready to start encrypting your files.\nWhether to proceed to work [Y/n]: ")
            if answer_to_encode == "Y" or answer_to_encode == "y":
                print("[!] Files with passwords will encode and moved to your flash now [!]")
                for filename in os.listdir('.'):
                    with open("key.txt", "rb") as file:
                        key = file.read()
                    if 'pass' in filename.lower():
                        print(f"[*] File encryption process - {filename}")
                        encrypt_file(Fernet(key), filename)
                        os.system(f'rm {filename}')
                print("[|] All files were encrypted!\nNow program will move it on flash drive...")
                while True:
                    drive = input("[?] Enter the name of the drive: ")
                    if os.path.ismount(f"/Volumes/{drive}"):
                        for filename in os.listdir('.'):
                            if 'pass' in filename.lower():
                                if os.path.isfile(filename):
                                    print(f"[*] Moving {filename} on flash drive...")
                                    mover(drive, filename)

                        print("[***] Complete!")
                        return
                    else:
                        print("[!] There is no drive like that, please retype...")

            elif answer_to_encode == "n":
                print("[-] Returning to main menu...")
                """main menu func"""
                return
            else:
                print("[!] Try again")
                return 0
        elif answ == "n":
            print("[*] Finishing program...")
            return 0
        else:
            print("[!] No answer like that")
            return 0

def main_menu():
    return "This is main menu..."
main()