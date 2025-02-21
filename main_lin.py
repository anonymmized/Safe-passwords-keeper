from functools import wraps
from cryptography.fernet import Fernet
from key_gen import key_generation
from enc_dec import encrypt_file, decrypt_file
import os
import time
import sys
import shutil
import getpass  # Import getpass to get the username

RED = "\033[91m"
END = "\033[0m"

key_name = "key.txt"
working_directory = ""
working_directory_file = "working_directory.txt"


def load_working_directory():
    """Loads the working directory from a file if it exists."""
    global working_directory
    if os.path.isfile(working_directory_file):
        with open(working_directory_file, 'r') as file:
            working_directory = file.read().strip()
        print(f"[*] Loaded working directory: '{working_directory}'")
    else:
        print("[*] No previous working directory found.")


def save_working_directory():
    """Saves the current working directory to a file."""
    with open(working_directory_file, 'w') as file:
        file.write(working_directory)


def key_check():
    """Generates a key if it doesn't exist."""
    key_path = os.path.join(working_directory, key_name)
    if not os.path.isfile(key_path):
        print("[*] Key will be generated now. Processing...")
        key_generation(key_path)
        time.sleep(2)
        print("[!] The key was generated under the name key.txt in the working directory.")


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


def set_working_directory():
    global working_directory
    load_working_directory()

    if not working_directory:
        new_directory = input("Enter the path where you want to create or set the working directory 'SPK-work': ")
        working_directory = os.path.join(new_directory, 'SPK-work')
        os.makedirs(working_directory, exist_ok=True)
        os.makedirs(os.path.join(working_directory, "source_files"), exist_ok=True)
        os.makedirs(os.path.join(working_directory, "processed_files"), exist_ok=True)
        print(f"[*] Working directory '{working_directory}' created successfully.")
    else:
        change_dir = input("[?] Do you want to change the working directory? [Y/n]: ")
        if change_dir.lower() == "y":
            new_directory = input("Enter the new path where you want to set the working directory 'SPK-work': ")
            working_directory = os.path.join(new_directory, 'SPK-work')
            os.makedirs(working_directory, exist_ok=True)
            os.makedirs(os.path.join(working_directory, "source_files"), exist_ok=True)
            os.makedirs(os.path.join(working_directory, "processed_files"), exist_ok=True)
            print(f"[*] Working directory '{working_directory}' created successfully.")

    save_working_directory()


def encrypt_move():
    time.sleep(2)
    answer_to_encode = input(
        "[!] Preparation is completed\nNow the program is ready to start encrypting your files.\nWhether to proceed to work [Y/n]: ")

    if answer_to_encode.lower() == "y":
        print("[!] Files with passwords will encode now [!]")
        files_to_encrypt = []

        for filename in os.listdir(os.path.join(working_directory, "source_files")):
            if 'pass' in filename.lower() and filename.lower().endswith('.txt') and not filename.startswith('._'):
                files_to_encrypt.append(filename)

        if not files_to_encrypt:
            print("[!] No valid .txt files with 'pass' found to encrypt.")
            return

        with open(os.path.join(working_directory, key_name), "rb") as file:
            key = file.read()
            f = Fernet(key)

        # Get the current user's name
        user_name = getpass.getuser()
        drive_name = input(f"[?] Enter the name of the drive (mount point) under '/media/{user_name}': ")
        drive_path = f"/media/{user_name}/{drive_name}"

        if not os.path.ismount(drive_path):
            print(f"[!] Drive '{drive_name}' is not mounted. Please make sure the drive is connected.")
            return

        for filename in files_to_encrypt:
            try:
                print(f"[*] File encryption process - {filename}")
                encrypt_file(f, filename, os.path.join(working_directory, "source_files"))

                os.remove(os.path.join(working_directory, "source_files", filename))
                print(f"[+] Original file {filename} removed.")

                encrypted_filename = filename.replace('.txt', '.enc')
                encrypted_file_path = os.path.join(working_directory, "source_files", encrypted_filename)

                if os.path.exists(encrypted_file_path):
                    destination_file_path = os.path.join(drive_path, encrypted_filename)
                    shutil.move(encrypted_file_path, destination_file_path)
                    print(f"[+] Moved encrypted file {encrypted_filename} to drive {drive_name}.")
                else:
                    print(f"[!] Encrypted file {encrypted_file_path} does not exist after encryption.")

            except Exception as e:
                print(f"[!] Error encrypting or moving {filename}: {e}")

        print("[|] All files were processed!")

    elif answer_to_encode.lower() == "n":
        print("[-] Returning to main menu...")


def decrypt_return():
    time.sleep(2)
    answer_to_decode = input(
        "[!] Preparation is completed\nNow the program is ready to start decrypting your files.\nWhether to proceed to work [Y/n]: ")

    if answer_to_decode.lower() == "y":
        print("[!] Files will be decrypted now [!]")
        files_to_decrypt = []

        # Get the current user's name
        user_name = getpass.getuser()
        drive = input(f"[?] Enter the name of the drive (mount point) under '/media/{user_name}': ")
        drive_path = f"/media/{user_name}/{drive}"

        if os.path.ismount(drive_path):
            print(f"[+] Drive {drive} is mounted. Searching for .enc files...")
            for filename in os.listdir(drive_path):
                if filename.endswith('.enc') and not filename.startswith('._'):
                    enc_file_path = os.path.join(drive_path, filename)
                    destination_path = os.path.join(working_directory, "processed_files", filename)
                    shutil.move(enc_file_path, destination_path)
                    files_to_decrypt.append(destination_path)
                    print(f"[+] Moved encrypted file {filename} to processed_files directory.")

        for filename in os.listdir(os.path.join(working_directory, "processed_files")):
            if filename.endswith('.enc') and not filename.startswith('._'):
                files_to_decrypt.append(os.path.join(working_directory, "processed_files", filename))

        if not files_to_decrypt:
            print("[!] No valid .enc files found to decrypt.")
            return

        with open(os.path.join(working_directory, key_name), "rb") as file:
            key = file.read()
            f = Fernet(key)

        for filepath in files_to_decrypt:
            filename = os.path.basename(filepath)
            try:
                print(f"[*] File decryption process - {filename}")
                decrypt_file(f, filepath, os.path.join(working_directory, "processed_files"))
                print(f"[+] Decrypted file {filename} removed from processing location.")
            except Exception as e:
                print(f"[!] Error decrypting or removing {filename}: {e}")

        print("[|] All files were processed!")

    elif answer_to_decode.lower() == "n":
        print("[-] Returning to main menu...")


@red_output
def menu_lin():
    """Displays the main menu and handles user choices."""
    global working_directory
    project_name = (
        " ____   _    ____ ____    _  _______ _____ ____  _____ ____  \n"
        "|  _ \\ / \\  / ___/ ___|  | |/ / ____| ____|  _ \\| ____|  _ \\ \n"
        "| |_) / _ \\ \\___ \\___ \\  | ' /|  _| |  _| | |_) |  _| | |_) |\n"
        "|  __/ ___ \\ ___) |__) | | . \\| |___| |___|  __/| |___|  _ < \n"
        "|_| /_/   \\_\\____/____/  |_|\\_\\_____|_____|_|   |_____|_| \\_|\n"
    )
    print(project_name)

    print("")
    print("[#] This program is moving your files with 'pass' in filenames to flash drive!\n")

    key_check()

    action = input("[1] Encrypt and move\n[2] Decrypt and return\n[1|2]: ")

    if action == "1":
        encrypt_move()
    elif action == "2":
        decrypt_return()
    else:
        print("[*] Invalid input. Please try again.")
        menu_lin()

set_working_directory()
menu_lin()