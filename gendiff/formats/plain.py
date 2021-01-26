import gendiff.gendiff as gendiff


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return "'{}'".format(value)
    return to_srting(value)


def make_string(diff, parent=[]):
    strings = []

    for key, (type_of_changing, value) in sorted(diff.items()):
        parents = parent + [key]
        path = '.'.join(parents)

        if type_of_changing == gendiff.NESTED:
            strings.append("{}".format(
                make_string(value, parent=parents)))
        elif type_of_changing == gendiff.ADDED:
            strings.append("{}' was added with value: {}".format(
                path, format_value(value)))
        elif type_of_changing == gendiff.REMOVED:
            strings.append("{}' was removed".format(path))
        elif type_of_changing == gendiff.CHANGED:
            old, new = value
            strings.append("{}' was updated. From {} to {}".format(
                    path, format_value(old), format_value(new))
            )

    return '\n'.join(strings)


def to_srting(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result


def add_prefix(strings):
    result = strings.split('\n')
    for index, elem in enumerate(result):
        result[index] = "Property '" + elem
    return result


def formatter(diff):
    strings = make_string(diff)
    new_strings = add_prefix(strings)

    return '\n'.join(new_strings) + '\n'
