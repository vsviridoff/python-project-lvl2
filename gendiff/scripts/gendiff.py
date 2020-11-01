#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
    '-f', '--format',
    help='set format of output'
)
parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
