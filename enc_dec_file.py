import os
from cryptography.fernet import Fernet

def encrypt_file(key, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = key.encrypt(data)

    filename_without_ext = os.path.splitext(file_path)[0]

    with open(f'{filename_without_ext}.enc', 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(key, file_path):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = key.decrypt(encrypted_data)

    filename_without_ext = os.path.splitext(file_path)[0]

    with open(f'{filename_without_ext}.txt', 'wb') as file:
        file.write(decrypted_data)


"""
for filename in os.listdir('.'):
    with open("key.txt", "rb") as file:
        key = file.read()
    if 'pass' in filename.lower():
        print(f"[*] Процесс шифра файла - {filename}")
        encrypt_file(Fernet(key), filename)
        os.system(f'rm {filename}')
"""

"""
for filename in os.listdir('.'):
    with open("key.txt", "rb") as file:
        key = file.read()
    if '.enc' in filename.lower():
        print(f"[*] Процесс дешифровки файла - {filename}")
        decrypt_file(Fernet(key), filename)
"""