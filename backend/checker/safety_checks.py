import re

def run_safety_checks(file_path):
    warnings = []

    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
    except Exception:
        return warnings

    # Infinite loop check
    if 'while True' in content and 'sleep' not in content:
        warnings.append('Infinite loop without sleep detected')

    # Joint safety check (context-aware)
    joint_patterns = [
        r'joint',
        r'joint_position',
        r'joint_angle'
    ]

    for pattern in joint_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            values = re.findall(r'[-+]?[0-9]*\.?[0-9]+', content)
            for val in values:
                try:
                    if abs(float(val)) > 3.14:
                        warnings.append(f'Joint value {val} exceeds safe limit')
                except ValueError:
                    pass
            break  # avoid duplicate warnings

    return warnings
