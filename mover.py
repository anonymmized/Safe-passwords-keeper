"""/Volumes/pass_keeper"""
import os

def mover(drive, filepath):
    cur_dir = "/Volumes"
    folder_path = os.path.join(cur_dir, drive)
    os.system(f"mv {filepath} {folder_path}")
