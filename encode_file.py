import os

def encrypt_file(key, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = key.encrypt(data)

    filename_without_ext = os.path.splitext(file_path)[0]

    with open(f'{filename_without_ext}.enc', 'wb') as file:
        file.write(encrypted_data)


