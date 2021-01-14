from gendiff.file_parcer import get_file_data
from gendiff.formatter import get_format


EQUAL, CHANGED, REMOVED, ADDED, NESTED = (
    'equal', 'changed', 'ramoved', 'added', 'nested'
)


def build(first_data, second_data):
    diff = {}
    common_keys = first_data.keys() & second_data.keys()
    removed_keys = first_data.keys() - second_data.keys()
    added_keys = second_data.keys() - first_data.keys()

    for key in common_keys:
        value1 = first_data[key]
        value2 = second_data[key]
        if isinstance(value1, dict) and isinstance(value2, dict):
            new_value = (NESTED, build(value1, value2))
        elif value1 == value2:
            new_value = (EQUAL, value1)
        else:
            new_value = (CHANGED, (value1, value2))
        diff[key] = new_value
    for key in removed_keys:
        diff[key] = (REMOVED, first_data[key])
    for key in added_keys:
        diff[key] = (ADDED, second_data[key])
    return diff


def generate_diff(first_file, second_file, output_format):
    first_data = get_file_data(first_file)
    second_data = get_file_data(second_file)
    unformated_diff = build(first_data, second_data)
    format_diff = get_format(output_format)
    return format_diff.formatter(unformated_diff)
