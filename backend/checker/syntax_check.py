import subprocess
import os


def check_python_syntax(path):
    result = subprocess.run(["flake8", path], capture_output=True, text=True)
    return result.stdout or "No syntax issues found"




def check_cpp_syntax(file_path):
    result = subprocess.run(["g++", "-fsyntax-only", file_path], capture_output=True, text=True)
    return result.stderr or "No syntax issues found"