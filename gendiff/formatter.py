from gendiff.formats import stylish


def get_format(output_format):
    if output_format == 'stylish':
        format = stylish
    else:
        raise ValueError('Invalid output format')

    return format
