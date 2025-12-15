import re


def detect_ros_entities(file_path):
entities = {'publishers': [], 'subscribers': []}
with open(file_path, 'r', errors='ignore') as f:
content = f.read()
entities['publishers'] = re.findall(r'create_publisher|Publisher', content)
entities['subscribers'] = re.findall(r'create_subscription|Subscriber', content)
return entities