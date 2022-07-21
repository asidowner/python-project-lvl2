#!/usr/bin/env python
import argparse

_MAIN_DESCRIPTION = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(description=_MAIN_DESCRIPTION)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    print(args)
