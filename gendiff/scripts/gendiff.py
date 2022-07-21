#!/usr/bin/env python
import argparse

_MAIN_DESCRIPTION = 'Compares two configuration files and shows a difference.'
_FORMAT_ARG_HELP = 'set format of output'


def main():
    parser = argparse.ArgumentParser(description=_MAIN_DESCRIPTION)
    parser.add_argument('-f', '--format',
                        type=str, help=_FORMAT_ARG_HELP)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    print(args)
