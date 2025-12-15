import os


def check_ros_structure(package_path):
    errors = []
    if not os.path.exists(os.path.join(package_path, 'package.xml')):
        errors.append('Missing package.xml')
    if not (os.path.exists(os.path.join(package_path, 'setup.py')) or
        os.path.exists(os.path.join(package_path, 'CMakeLists.txt'))):
            errors.append('Missing setup.py or CMakeLists.txt')
    return errors