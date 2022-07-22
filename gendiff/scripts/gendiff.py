#!/usr/bin/env python
import argparse
from argparse import ArgumentParser, Namespace
from gendiff.generate_diff import generate_diff

_MAIN_DESCRIPTION = 'Compares two configuration files and shows a difference.'
_FORMAT_ARG_HELP = 'set format of output'


def main():
    args = _get_command_args()
    diff = generate_diff(
        format_=args.get('format'),
        first_file_path=args.get('first_file'),
        second_file_path=args.get('second_file')
    )
    print(diff)


def _get_command_args() -> dict:
    parser: ArgumentParser = \
        argparse.ArgumentParser(description=_MAIN_DESCRIPTION)
    parser.add_argument('-f', '--format',
                        type=str, help=_FORMAT_ARG_HELP,
                        default='stylish')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args: Namespace = parser.parse_args()
    return vars(args)
