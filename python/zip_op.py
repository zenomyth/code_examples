import sys
import tempfile
import zipfile
from pathlib import Path

def zip_folder():
    # Replace the folder path and password with your own values
    folder_path = Path("c:/Work/Source/git/CTC/bst-bsts-core/bst_ai_integration/src/bst_ai_integration/offline_verification/example_input/")
    file1 = folder_path.joinpath("oci_Bosch_APP30_WRD_BHI260_Mlmodel_test.fw")
    file2 = folder_path.joinpath("oci_Bosch_APP30_WRD_BHI260_Mlmodel_test2.fw")
    file3 = folder_path.joinpath("reference_data.h")
    # password = "#bst#generated#test#data#"

    # Define the name and path of the output zip file
    zip_file_path = folder_path.joinpath("internal_verification.dat")

    # Create a new zip file with the given password
    with zipfile.ZipFile(zip_file_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        # zip_file.setpassword(bytes(password, 'utf-8'))
        zip_file.write(file1, arcname="oci_Bosch_APP30_WRD_BHI260_Mlmodel_test.fw")
        zip_file.write(file2, arcname="oci_Bosch_APP30_WRD_BHI260_Mlmodel_test2.fw")
        zip_file.write(file3, arcname="reference_data.h")

    print("Zip file created successfully!")

def unzip_to_temp_dir():
    zip_file_path = "c:/Work/Source/git/CTC/bst-bsts-core/bst_ai_integration/src/bst_ai_integration/offline_verification/example_input/internal_verification.dat"
    # password = "#bst#generated#test#data#"

    # create a temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        print("tmp_dir:", tmp_dir)
        # extract the contents of the zip file to the temporary directory
        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            # zip_file.setpassword(bytes(password, "utf-8"))
            zip_file.extractall(tmp_dir)

        # do something with the contents of the zip file
        # for example, print the contents of each file in the directory
        for file_name in Path(tmp_dir).glob("**/*"):
            print(file_name)

        # remove the temporary directory and its contents
        # this will automatically remove the extracted files
        # as well as the temporary directory itself

def main():
    # zip_folder()
    unzip_to_temp_dir()

if __name__ == "__main__":
    sys.exit(main())
