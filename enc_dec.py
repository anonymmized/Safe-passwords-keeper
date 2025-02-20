import os

def encrypt_file(f, filename, source_folder):
    """Encrypt a file."""
    file_path = os.path.join(source_folder, filename)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    encrypted_filename = filename.replace('.txt', '') + ".enc"

    with open(os.path.join(source_folder, encrypted_filename), "wb") as file:
        file.write(encrypted_data)


def decrypt_file(key, file_path, to_path):
    """Decrypts a file and saves the decrypted data."""
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = key.decrypt(encrypted_data)

        filename_without_ext = os.path.splitext(os.path.basename(file_path))[0]

        returned_file_path = os.path.join(to_path, f'{filename_without_ext}.txt')

        os.makedirs(to_path, exist_ok=True)

        with open(returned_file_path, 'wb') as file:
            file.write(decrypted_data)

        print(f"[*] Decryption of {file_path} is complete.")

        os.remove(file_path)

    except FileNotFoundError:
        print(' ')