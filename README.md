# Safe-passwords-keeper

This project helps you securely store all your passwords in one place on a storage device.

**How it works:** Insert a flash drive, encrypt password files, and move the encrypted files to the storage device.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/anonymmized/Safe-passwords-keeper 
    cd Safe-passwords-keeper
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the main file:**

    ```bash
    python main.py
    ```

    A key will be generated upon the first run for file encryption.

    **Important Security Notes:**
    *   **Key Location:** If you move the key file from the project directory, the program will not be able to find it.
    *   **Key Loss:** If you lose the key, you will be unable to decrypt your passwords. It's highly recommended to securely store the key both on the flash drive *and* on your device as a backup.

2.  **Program Options:** The program has two main options:

    *   `[1] - Encrypt and Move to Flash Drive`
    *   `[2] - Decrypt and Move Back to Device`


### Encrypt and Move to Flash Drive

This option searches for all files in the current directory containing the string `pass`.  It encrypts these files, deletes the originals, and moves the encrypted versions to the specified flash drive.

    *(Example Screenshot - Replace with your actual screenshot)*
    ![Screenshot 2](YOUR_SCREENSHOT_LINK_OR_IMAGE_FILE)  # Replace with the URL or relative path to your screenshot

    1.  **Specify Flash Drive:**  You will be prompted to enter the correct name of your flash drive during the move operation.
    2.  **Successful Transfer:**  The files will be successfully moved to the flash drive after you enter the correct drive name.

    **Important Safety Advice:**  Always unmount your flash drive (safely remove hardware) before physically removing it.  Failing to do so could lead to data corruption.

### Decrypt and Move Back to Device

This option moves all files containing the string `pass` from the flash drive back to your device.  The decrypted files will be placed in the `returned_files` directory.  The decrypted files will have a `.txt` extension.

    **Important Note:**  You will need to specify the correct name of your flash drive to perform the transfer.

---

**License:**

This project is licensed under the [MIT License](LICENSE).  Please refer to the `LICENSE` file in the repository for more information.  (Include the `LICENSE` file in the root of your project.)