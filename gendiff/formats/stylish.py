import gendiff.diff_generator as gendiff


ADDED_PREFIX, REMOVED_PREFIX, EQUAL_PREFIX = ('+', '-', ' ')


def formatter(diff):
    return format_diff(diff)


def format_items(value, ident):
    result = []

    for key, value in value.items():

        def get_nested_items(value, ident):
            for k, v in value.items():
                ident = ident + 4
                if isinstance(v, dict):
                    v = get_nested_items(v, ident)
                item = "\n    {ident}{key}: {value}\n{ident}".format(
                    ident=' ' * (ident + 4),
                    key=k,
                    value=to_string(v)
                )

            return '{' + item + '}'

        if isinstance(value, dict):
            value = get_nested_items(value, ident)
        result.append("\n    {ident}{key}: {value}".format(
            ident=' ' * (ident + 4),
            key=key,
            value=to_string(value)
        ))

    return '{' + ''.join(result) + '\n' + (' ' * (ident + 4)) + '}'


def format_value(value, ident):
    if isinstance(value, dict):
        return format_items(value, ident)
    else:
        return to_string(value)


def make_string(diff, ident=0):
    strings = []

    for key, (type_of_changing, value) in sorted(diff.items()):

        def make_line(prefix, value_to_show):
            return '  {ident}{prefix} {key}: {value}'.format(
                ident=' ' * ident,
                prefix=prefix,
                key=key,
                value=format_value(value_to_show, ident)
            )

        if type_of_changing == gendiff.NESTED:
            strings.append('{ident}{key}: {{\n{value}\n{ident}}}'.format(
                ident=' ' * (ident + 4),
                key=key,
                value=make_string(value, ident + 4)
            ))
        elif type_of_changing == gendiff.EQUAL:
            strings.append(make_line(EQUAL_PREFIX, value))
        elif type_of_changing == gendiff.CHANGED:
            old, new = value
            strings.append(make_line(REMOVED_PREFIX, old))
            strings.append(make_line(ADDED_PREFIX, new))
        elif type_of_changing == gendiff.REMOVED:
            strings.append(make_line(REMOVED_PREFIX, value))
        elif type_of_changing == gendiff.ADDED:
            strings.append(make_line(ADDED_PREFIX, value))

    return '\n'.join(strings)


def format_diff(diff):
    return '{\n' + make_string(diff) + '\n}\n'


def to_string(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        return 'false'
    else:
        result = str(value)

    return result
