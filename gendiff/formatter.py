from gendiff.formats import stylish, plain, json


def get_format(output_format):
    if output_format == 'stylish':
        format = stylish
    elif output_format == 'plain':
        format = plain
    elif output_format == 'json':
        format = json
    else:
        raise ValueError('Invalid output format')

    return format
