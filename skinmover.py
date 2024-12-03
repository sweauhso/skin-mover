import os
import zipfile

# Define the source directory and destination directory
source_dir = r"path to skins"
destination_dir = r"path to installed folder in cslol"

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Loop through each champion folder and their `.zip` files
for champion_folder in os.listdir(source_dir):
    champion_path = os.path.join(source_dir, champion_folder)
    if os.path.isdir(champion_path):  # Ensure it's a folder
        for file_name in os.listdir(champion_path):
            if file_name.lower() == "chromas":  # Skip the chromas folder
                continue
            file_path = os.path.join(champion_path, file_name)
            # Check if the file is a zip file
            if zipfile.is_zipfile(file_path):
                # Create a folder in the destination directory with the same name as the zip file (without .zip extension)
                zip_folder_name = os.path.splitext(file_name)[0]  # Get the zip file name without extension
                zip_folder_path = os.path.join(destination_dir, zip_folder_name)
                os.makedirs(zip_folder_path, exist_ok=True)
                
                # Extract the zip file into its own folder
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(zip_folder_path)
                    print(f"Extracted: {file_name} into {zip_folder_path}")
