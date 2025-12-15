import json
import os


def generate_report(errors, warnings, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    report = {'errors': errors, 'warnings': warnings}
    with open(os.path.join(output_dir, 'report.json'), 'w') as f:
        json.dump(report, f, indent=4)
    with open(os.path.join(output_dir, 'report.txt'), 'w') as f:
        f.write(str(report))
    return report