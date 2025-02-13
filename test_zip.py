import glob
import os
import zipfile


def create_individual_archives(filepaths):
    for filepath in filepaths:
        base_filename = os.path.splitext(os.path.basename(filepath))[0] + ".zip"
        with zipfile.ZipFile(base_filename, "w") as archive:
            archive.write(filepath, arcname=os.path.basename(filepath))

def find_files_with_pass(root_dir):
    filepaths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if "pass" in filename:
                filepath = os.path.join(dirpath, filename)
                filepaths.append(filepath)
    return filepaths

if __name__ == "__main__":
    root_dir = "."
    filepaths = find_files_with_pass(root_dir)
    create_individual_archives(filepaths)