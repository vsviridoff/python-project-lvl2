import os
import json
import yaml


def get_file_data(file):
    _, file_extentions = os.path.splitext(file)
    if file_extentions == '.json':
        data = json.load(open(file))
    elif file_extentions == '.yaml' or file_extentions == '.yml':
        data = yaml.safe_load(open(file))
    return data
