from functools import wraps
from encode_file import encrypt_file
from cryptography.fernet import Fernet
from key_gen import key_generation
import os
from mover import mover
import time
import sys


RED = "\033[91m"
END = "\033[0m"

key_name = "key.txt"
def key_check():
    if not os.path.isfile(key_name):
        print("[*] Key will generate now. Processing...")
        key_generation()
        time.sleep(2)
        print("[!] The key was generated under the name key.txt")


def red_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_stdout = sys.stdout

        class Buffer:
            def write(self, text):
                original_stdout.write(RED + text + END)
            def flush(self):
                try:
                    original_stdout.flush()
                except AttributeError:
                    pass

        sys.stdout = Buffer()
        result = func(*args, **kwargs)
        sys.stdout = original_stdout
        return result
    return wrapper

@red_output
def menu():
    project_name = (
        " ____   _    ____ ____    _  _______ _____ ____  _____ ____  \n"
        "|  _ \\ / \\  / ___/ ___|  | |/ / ____| ____|  _ \\| ____|  _ \\ \n"
        "| |_) / _ \\ \\___ \\___ \\  | ' /|  _| |  _| | |_) |  _| | |_) |\n"
        "|  __/ ___ \\ ___) |__) | | . \\| |___| |___|  __/| |___|  _ < \n"
        "|_| /_/   \\_\\____/____/  |_|\\_\\_____|_____|_|   |_____|_| \\_|\n"
    )
    print(project_name)
    print("[#] This program moving your files with 'pass' in filenames to flash drive!\n")
    action = int(input("[1] Encrypt and move\n[2] Decrypt and return\n[1|2]: "))

    while True:
        if action == 1:
            encrypt_move()
        elif action == 2:
            pass # decrypt_remove
        else:
            print("[*] Try again")


def encrypt_move():
    time.sleep(2)
    answer_to_encode = input("[!] Preparation is completed\nNow program is ready to start encrypting your files.\nWhether to proceed to work [Y/n]: ")
    if answer_to_encode == "Y" or answer_to_encode == "y":
        time.sleep(1)
        print("[!] Files with passwords will encode now [!]")
        files = os.listdir('.')

        for filename in os.listdir('.'):
            with open("key.txt", "rb") as file:
                key = file.read()
                if 'pass' in filename.lower():
                    if os.path.splitext(filename)[1].lower() == '.txt':
                        time.sleep(1)
                        print(f"[*] File encryption process - {filename}")
                        encrypt_file(Fernet(key), filename)
                        os.system(f'rm {filename}')

            if any('pass' in file.lower() for file in files):
                print("[|] All files were encrypted!\nNow program will move it on flash drive...")
            else:
                print("[!] There is nothing to encrypt")
                raise FileNotFoundError

            while True:
                time.sleep(1)
                drive = input("[?] Enter the name of the drive: ")
                if os.path.ismount(f"/Volumes/{drive}"):
                    for filename in os.listdir('.'):
                        if 'pass' in filename.lower():
                            if os.path.isfile(filename):
                                time.sleep(1)
                                print(f"[*] Moving {filename} on flash drive...")
                                mover(drive, filename)
                                print("[***] Complete!")
                                return

                else:
                    time.sleep(1)
                    print("[!] There is no drive like that, please retype...")

    elif answer_to_encode == "n":
        time.sleep(1)
        print("[-] Returning to main menu...")
        menu()

    else:
        time.sleep(1)
        print("[!] Try again")


def decrypt_return():
    time.sleep(2)
    answ = input("[*] Preparation is completed\n Do you want to return your files [Y/n]: ")

    while True:

        if answ == "y" or answ == "Y":
            pass

        elif answ == "n":
            print("[*] Finishing program...")
            return 0

        else:
            print("[!] No answer like that")


key_check()
menu()