import zipfile
import os
import shutil

def unzip_package(zip_path, extract_base):
    """
    Extracts ZIP into a clean, dedicated folder named after the ZIP file.
    """
    zip_name = os.path.splitext(os.path.basename(zip_path))[0]
    extract_path = os.path.join(extract_base, zip_name)

    # Clean old extraction if exists
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)

    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    return extract_path
