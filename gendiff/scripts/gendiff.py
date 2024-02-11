#!/usr/bin/env python3


from gendiff.parsing import parsing
from gendiff import generate_diff


def main():
    file1, file2, format = parsing()
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
