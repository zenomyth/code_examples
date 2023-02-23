import tempfile
import zipfile
import os

# specify the path of the zip file
zip_file_path = 'path/to/zipfile.zip'
password = ""

# create a temporary directory
with tempfile.TemporaryDirectory() as tmp_dir:
    # extract the contents of the zip file to the temporary directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.setpassword(bytes(password, 'utf-8'))
        zip_file.extractall(tmp_dir)

    # do something with the contents of the zip file
    # for example, print the contents of each file in the directory
    for file_name in os.listdir(tmp_dir):
        file_path = os.path.join(tmp_dir, file_name)
        with open(file_path, 'r') as f:
            print(f.read())

    # remove the temporary directory and its contents
    # this will automatically remove the extracted files
    # as well as the temporary directory itself

import zipfile

# Replace the folder path and password with your own values
folder_path = "/path/to/your/folder"
password = "your_password"

# Define the name and path of the output zip file
zip_file_path = "/path/to/output/zip/file.zip"

# Create a new zip file with the given password
with zipfile.ZipFile(zip_file_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zip_file:
    zip_file.setpassword(bytes(password, 'utf-8'))
    # Add all files in the folder to the zip file
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            zip_file.write(os.path.join(root, file))

print("Zip file created successfully!")

