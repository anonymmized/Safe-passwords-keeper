from functools import wraps
from cryptography.fernet import Fernet
from key_gen import key_generation
from enc_dec import encrypt_file, decrypt_file
from mover import mover_to_drive, mover_from_drive
import os
import time
import sys

RED = "\033[91m"
END = "\033[0m"

key_name = "key.txt"

def key_check():
    """Generates a key if it doesn't exist."""
    if not os.path.isfile(key_name):
        print("[*] Key will generate now. Processing...")
        key_generation()
        time.sleep(2)
        print("[!] The key was generated under the name key.txt")


def red_output(func):
    """Decorator to print output in red color."""
    @wraps(func)
    def wrapper():
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
        result = func()
        sys.stdout = original_stdout
        return result
    return wrapper


def encrypt_move():
    time.sleep(2)
    answer_to_encode = input("[!] Preparation is completed\nNow program is ready to start encrypting your files.\nWhether to proceed to work [Y/n]: ")

    if answer_to_encode.lower() == "y":
        print("[!] Files with passwords will encode now [!]")
        files_to_process = []

        for filename in os.listdir('.'):
            if 'pass' in filename.lower() and os.path.splitext(filename)[1].lower() == '.txt':
                files_to_process.append(filename)

        if not files_to_process:
            print("[!] No files with 'pass' and .txt extension found to encrypt.")
            return


        with open("key.txt", "rb") as file:
            key = file.read()
            f = Fernet(key)

        for filename in files_to_process:
            try:
                time.sleep(1)
                print(f"[*] File encryption process - {filename}")
                encrypt_file(f, filename)
                os.remove(filename)
                print(f"[+] Original file {filename} removed")

            except Exception as e:
                print(f"[!] Error encrypting or removing {filename}: {e}")
                continue

        print("[|] All files were encrypted!\nNow program will move them to the flash drive...")
        while True:
            time.sleep(1)
            drive = input("[?] Enter the name of the drive: ")
            drive_path = f"/Volumes/{drive}"
            if os.path.ismount(drive_path):
                for filename in files_to_process:
                    encrypted_file = os.path.splitext(filename)[0] + ".enc"
                    if os.path.exists(encrypted_file):
                        try:
                            time.sleep(1)
                            print(f"[*] Moving {encrypted_file} to flash drive...")
                            mover_to_drive(drive, encrypted_file)
                            print("[***] Complete!")
                        except Exception as e:
                            print(f"[!] Error moving {encrypted_file} to drive: {e}")
                    else:
                        print(f"[!] Encrypted file {encrypted_file} not found.  Skipping.")
                break
            else:
                time.sleep(1)
                print("[!] There is no drive like that, please retype...")


    elif answer_to_encode.lower() == "n":
        time.sleep(1)
        print("[-] Returning to main menu...")
        menu()
    else:
        time.sleep(1)
        print("[!] Invalid input. Please try again.")


def decrypt_return():
    """Decrypts files from a flash drive and handles user interaction."""
    time.sleep(2)
    answer_to_decode = input("[!] Preparation is completed\nNow program is ready to start decrypting your files.\nWhether to proceed to work [Y/n]: ")

    if answer_to_decode.lower() == "y":
        print("[!] Files with passwords will return now [!]")
        drive = input("[?] Enter the name of the drive: ")
        drive_path = f"/Volumes/{drive}"

        if os.path.exists(drive_path):
            print(f"Drive {drive} found.")
            files_to_decrypt = []
            for filename in os.listdir(drive_path):
                if 'pass' in filename.lower() and filename.endswith(".enc"):
                    files_to_decrypt.append(filename)

            if not files_to_decrypt:
                print("[!] No encrypted files with 'pass' found on the drive.")
                return


            if not os.path.exists("returned_files"):
                os.makedirs("returned_files")

            for filename in files_to_decrypt:
                try:
                    time.sleep(1)
                    print(f"[*] Returning {filename} to device...")
                    mover_from_drive(drive, filename)
                    print("[***] Complete!")
                except Exception as e:
                    print(f"[!] Error moving {filename} from drive: {e}")
                    continue


            with open("key.txt", "rb") as file:
                key = file.read()
                f = Fernet(key)

            for filename in os.listdir('./returned_files'):
                if filename.endswith(".enc"):
                    try:
                        print(f"[*] The process of decryption of the file - {filename}")
                        decrypt_file(f, filename)
                    except Exception as e:
                        print(f"[!] Error decrypting {filename}: {e}")
                        continue

        else:
            print(f"Drive {drive} not found. Please check the name and try again.")
            return

    elif answer_to_decode.lower() == "n":
        time.sleep(1)
        print("[-] Returning to main menu...")
        menu()
    else:
        time.sleep(1)
        print("[!] Invalid input. Please try again.")

@red_output
def menu():
    """Displays the main menu and handles user choices."""
    project_name = (
        " ____   _    ____ ____    _  _______ _____ ____  _____ ____  \n"
        "|  _ \\ / \\  / ___/ ___|  | |/ / ____| ____|  _ \\| ____|  _ \\ \n"
        "| |_) / _ \\ \\___ \\___ \\  | ' /|  _| |  _| | |_) |  _| | |_) |\n"
        "|  __/ ___ \\ ___) |__) | | . \\| |___| |___|  __/| |___|  _ < \n"
        "|_| /_/   \\_\\____/____/  |_|\\_\\_____|_____|_|   |_____|_| \\_|\n"
    )
    print(project_name)
    print("[#] This program moving your files with 'pass' in filenames to flash drive!\n")
    action = input("[1] Encrypt and move\n[2] Decrypt and return\n[1|2]: ")

    if action == "1":
        encrypt_move()
    elif action == "2":
        decrypt_return()
    else:
        print("[*] Invalid input. Please try again.")
        menu()

key_check()
menu()