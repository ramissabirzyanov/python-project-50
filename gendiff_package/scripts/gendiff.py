#!/usr/bin/env python3


from gendiff_package.parsing import parsing
from gendiff_package.gendiff import generate_diff

def main():
    file1, file2 = parsing()
    print(generate_diff(file1, file2))
    
    
if __name__ == '__main__':
    main()

