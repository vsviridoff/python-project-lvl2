from gendiff.formats import stylish, plain


def get_format(output_format):
    if output_format == 'stylish':
        format = stylish
    elif output_format == 'plain':
        format = plain
    else:
        raise ValueError('Invalid output format')

    return format
