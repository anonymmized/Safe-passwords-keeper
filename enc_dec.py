import os

def encrypt_file(key, file_path):
    """Encrypts a single file."""
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = key.encrypt(data) # Use the Fernet instance
        filename_without_ext = os.path.splitext(file_path)[0]
        with open(f'{filename_without_ext}.enc', 'wb') as file:
            file.write(encrypted_data)
        print(f"[*] Encryption of {file_path} is complete.")

    except FileNotFoundError as err:
        print(f"Error encrypting {file_path}: {err}")
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")

def decrypt_file(key, file_path):
    """Decrypts a single file."""
    try:
        with open(f'./returned_files/{file_path}', "rb") as file:
            encrypted_data = file.read()
        decrypted_data = key.decrypt(encrypted_data) # use the Fernet instance
        filename_without_ext = os.path.splitext(file_path)[0]
        with open(f'./returned_files/{filename_without_ext}.txt', 'wb') as file:
            file.write(decrypted_data)
        print(f"[*] Decryption of {file_path} is complete.")
        os.remove(f'./returned_files/{file_path}') # Delete the encrypted file after decryption

    except FileNotFoundError as err:
        print(f"Error decrypting {file_path}: {err}")
    except Exception as e:
        print(f"Error decrypting {file_path}: {e}")
