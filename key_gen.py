from cryptography.fernet import Fernet
def key_generation():
    key = Fernet.generate_key()

    with open("key.txt", 'w') as f:
        f.write(key.decode())