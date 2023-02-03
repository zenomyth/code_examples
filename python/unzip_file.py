import zipfile

# ZipFile.extractall(path=None, members=None, pwd=None)
sdk_path = "C:\\Work\\Source\\git\\CTC\\bst-bsts-core\\bst_ai_integration\\src\\bst_ai_integration\\code_generator\\bhy2sdk_v1.1.8.0.zip"
with zipfile.ZipFile(sdk_path, 'r') as zip_ref:
    zip_ref.extractall(path="C:\\Work\\Data\\0\\bhi_sdk\\")