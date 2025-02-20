import os

def encrypt_file(f, filename, source_folder):
    """Encrypt a file."""
    # Полный путь к исходному файлу
    file_path = os.path.join(source_folder, filename)

    with open(file_path, "rb") as file:
        file_data = file.read()

    # Шифруем данные
    encrypted_data = f.encrypt(file_data)

    # Удаляем .txt из имени файла и сохраняем с расширением .enc
    encrypted_filename = filename.replace('.txt', '') + ".enc"  # Формируем новое имя файла

    # Сохраняем зашифрованный файл
    with open(os.path.join(source_folder, encrypted_filename), "wb") as file:
        file.write(encrypted_data)


def decrypt_file(key, file_path, to_path):
    """Decrypts a file and saves the decrypted data."""
    try:
        # Считываем зашифрованные данные
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        # Дешифруем данные
        decrypted_data = key.decrypt(encrypted_data)

        # Имя файла без расширения .enc
        filename_without_ext = os.path.splitext(os.path.basename(file_path))[0]

        # Сохраняем расшифрованный файл в указанной директории (to_path)
        returned_file_path = os.path.join(to_path, f'{filename_without_ext}.txt')

        # Убедитесь, что целевая директория существует
        os.makedirs(to_path, exist_ok=True)

        # Сохранение расшифрованных данных
        with open(returned_file_path, 'wb') as file:
            file.write(decrypted_data)  # Сохраняем расшифрованные данные

        print(f"[*] Decryption of {file_path} is complete.")

        # Удаляем зашифрованный файл после успешной расшифровки
        os.remove(file_path)

    except FileNotFoundError:
        print(' ')