"""/Volumes/pass_keeper"""
import os


def mover(filepath):        # <- сюда будет передаваться уже зашифрованный файл
    os.system(f"mv {filepath} /Volumes/pass_keeper")

filename = input("Enter filename: ")
print("[*] Moving your file on flash drive...")
mover(filename)
print("[***] Complete!")
