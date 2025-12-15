import os
from backend.utils.unzipper import unzip_package
from backend.checker.syntax_check import check_python_syntax
from backend.checker.ros_structure import check_ros_structure
from backend.checker.safety_checks import run_safety_checks
from backend.checker.report_generator import generate_report

UPLOAD_DIR = 'uploads'
OUTPUT_DIR = 'outputs/reports'

def find_ros_package_root(extract_path):
    """
    Finds the directory that contains package.xml
    """
    for root, dirs, files in os.walk(extract_path):
        if 'package.xml' in files:
            return root
    return None

def run_checker(zip_path):
    extract_path = unzip_package(zip_path, UPLOAD_DIR)

    errors = []
    warnings = []

    package_root = find_ros_package_root(extract_path)

    if package_root is None:
        errors.append('No ROS package found (package.xml missing)')
        return generate_report(errors, warnings, OUTPUT_DIR)

    # ✅ Correct structure check
    errors.extend(check_ros_structure(package_root))

    # ✅ File-level checks
    for root, _, files in os.walk(package_root):
        for file in files:
            full_path = os.path.join(root, file)
            if file.endswith('.py') and file != 'setup.py':
                warnings.append(check_python_syntax(full_path))
                warnings.extend(run_safety_checks(full_path))

    return generate_report(errors, warnings, OUTPUT_DIR)
