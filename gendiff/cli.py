import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output (stylish, json, plain)\ndefault: stylish',
        type=str
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    return parser
