from cryptography.fernet import Fernet


def key_generation(key_path):
    """Generate a new key and save it to the specified path."""
    key = Fernet.generate_key()

    # Сохраняем ключ в бинарном режиме
    with open(key_path, 'wb') as f:
        f.write(key)