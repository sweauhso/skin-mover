# Move and Extract Skins for CS LOL Manager

## Project Overview

This script processes a folder of League of Legends custom skin files, organized by champions. It extracts the `.zip` files from each champion's folder and organizes them into a single destination folder. Each `.zip` file is extracted into its own folder with the same name, enabling seamless integration with **CS LOL Manager** for using custom skins in the game.

---

## Folder Structure Before Processing

The original `skins` directory is expected to look like this:


---

## Folder Structure After Processing

The script will process the `skins` directory and create the following structure in the destination directory:


---

## How to Use

1. **Set Up Python**:
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Prepare the Script**:
   - Save the script provided in this repository to a file called `extract_skins.py`.

3. **Organize Your Folders**:
   - Place your `skins` folder (containing champion folders and `.zip` files) in an easily accessible directory.
   - Create a destination folder where the extracted skin files will be moved.

4. **Modify Script Paths**:
   - Edit the `source_dir` and `destination_dir` in `extract_skins.py` to match your setup:
     ```python
     source_dir = r"path/to/skins"
     destination_dir = r"path/to/destination"
     ```

5. **Run the Script**:
   - Open a terminal or command prompt.
   - Run the script using Python:
     ```bash
     python extract_skins.py
     ```

6. **Use CS LOL Manager**:
   - After running the script, copy the contents of the `destination` directory into the CS LOL Manager's **Skins** folder.
   - Launch CS LOL Manager and select the desired skins for your game.

---

## Important Notes

- The script **skips the "chromas" folder** in each champion directory to avoid unnecessary files.
- Each `.zip` file is extracted into a folder with the same name. Ensure no duplicate file names across champions to prevent overwriting.
- If you're unsure about the folder structure, double-check the source directory (`skins`) before running the script.

---

## Troubleshooting

- **No Extracted Files**:
  - Ensure the `.zip` files are valid and not corrupted.
  - Verify the `source_dir` and `destination_dir` paths in the script.

- **Duplicate Folder Names**:
  - If two zip files from different champion folders share the same name, their extracted contents might overwrite each other. Consider modifying the script to include the champion name in the folder names:
    ```python
    zip_folder_name = f"{champion_folder}_{os.path.splitext(file_name)[0]}"
    ```

---

## License

This script is provided as-is under the MIT license. It is free to use, modify, and distribute.

---

Enjoy your custom skins with **CS LOL Manager**! If you have any questions or encounter issues, feel free to reach out.
