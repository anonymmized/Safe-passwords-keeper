import os

def create_work_directory():
    path = input("Enter the path where you want to create the working directory 'SPK-work': ")
    work_dir = os.path.join(path, 'SPK-work')
    sub_dir_source = os.path.join(work_dir, "source_files")
    sub_dir_processed = os.path.join(work_dir, "processed_files")
    try:

        if not os.path.exists(work_dir):
            os.makedirs(work_dir)
            print(f"Working directory '{work_dir}' created successfully.")
            os.makedirs(sub_dir_source)
            os.makedirs(sub_dir_processed)
            print(
                f"Additional files have been created where you can store passwords: {sub_dir_source} and {sub_dir_processed}")

        else:
            print(f"Working directory '{work_dir}' already exists.")


    except Exception as e:
        print(f"An error occurred: {e}")

    return work_dir
