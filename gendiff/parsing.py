import argparse
import yaml
import json


def parsing():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        dest='format', default='stylish')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def read_file(path_to_file):
    if path_to_file.endswith(('.yaml', '.yml')):
        with open(path_to_file) as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    elif path_to_file.endswith('.json'):
        with open(path_to_file) as file:
            return json.load(file)
