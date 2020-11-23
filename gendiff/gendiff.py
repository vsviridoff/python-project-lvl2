import json


EQUAL, CHANGED, REMOVED, ADDED = (
    'equal', 'changed', 'ramoved', 'added'
)


def get_file_data(file):
    data = json.load(open(file))
    return data


def compair_files(first_data, second_data):
    diff = {}
    common_keys = first_data.keys() & second_data.keys()
    removed_keys = first_data.keys() - second_data.keys()
    added_keys = second_data.keys() - first_data.keys()

    for key in common_keys:
        value1 = first_data[key]
        value2 = second_data[key]
        if value1 == value2:
            new_value = (EQUAL, value1)
        else:
            new_value = (CHANGED, (value1, value2))
        diff[key] = new_value
    for key in removed_keys:
        diff[key] = (REMOVED, first_data[key])
    for key in added_keys:
        diff[key] = (ADDED, second_data[key])
    return diff


def make_string(diff, tab=2):
    strings = []
    tab = ' ' * tab
    for key, (type_of_changing, value) in sorted(diff.items()):
        if type_of_changing == EQUAL:
            strings.append(tab + "  {}: {}".format(key, value))
        if type_of_changing == CHANGED:
            old, new = value
            strings.append(tab + "- {}: {}".format(key, old))
            strings.append(tab + "+ {}: {}".format(key, new))
        if type_of_changing == REMOVED:
            strings.append(tab + "- {}: {}".format(key, value))
        if type_of_changing == ADDED:
            strings.append(tab + "+ {}: {}".format(key, value))
    return '{\n' + '\n'.join(strings) + '\n}\n'


def create_diff(first_file, second_file):
    first_data = get_file_data(first_file)
    second_date = get_file_data(second_file)
    unformated_diff = compair_files(first_data, second_date)
    formated_diff = make_string(unformated_diff)
    return formated_diff
