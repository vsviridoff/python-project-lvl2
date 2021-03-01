import os
import json
import yaml


def read_file(file):
    with open(file, 'r') as input_file:
        content = input_file.read()
    return content


def parse(content, format):
    if format == '.json':
        return json.loads(content)
    elif format == '.yaml' or format == '.yml':
        return yaml.safe_load(content)


def get_file_data(file):
    _, format = os.path.splitext(file)
    content = read_file(file)
    return parse(content, format)
