#!/usr/bin/env python
import argparse
from argparse import ArgumentParser, Namespace
from gendiff import generate_diff
from gendiff.lib.parser import SUPPORTED_SUFFIX

_MAIN_DESCRIPTION = 'Compares two configuration files and shows a difference.'
_FORMAT_ARG_HELP = 'set format of output'


def main():
    args: Namespace = _get_command_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        args.format
    )
    print(diff)


def _get_command_args() -> Namespace:
    parser: ArgumentParser = \
        argparse.ArgumentParser(description=_MAIN_DESCRIPTION)
    parser.add_argument('-f', '--format',
                        type=str, help=_FORMAT_ARG_HELP,
                        default='stylish', choices=['stylish', 'plain', 'json'])
    parser.add_argument('first_file', type=str,
                        help=f'Path to first file.'
                             f' Support file formats {SUPPORTED_SUFFIX}')
    parser.add_argument('second_file', type=str,
                        help=f'Path to second file.'
                             f' Support file formats {SUPPORTED_SUFFIX}')
    args: Namespace = parser.parse_args()
    return args
