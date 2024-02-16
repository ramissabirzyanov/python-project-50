import argparse
import yaml
import json
import os


def parsing():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        dest='format', default='stylish')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def get_extension(obj):
    _, extension = os.path.splitext(obj)
    return extension[1:]


def read_file(path_to_file):
    with open(path_to_file) as file:
        extension = get_extension(path_to_file)
        if extension == 'json':
            return json.load(file)
        elif extension == 'yaml' or 'yml':
            return yaml.load(file, Loader=yaml.FullLoader)
