from gendiff.formatters.formatting import formatting
from gendiff.parsing import read_file
from gendiff.make_diff import make_diff


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    data_file1 = read_file(path_to_file1)  # dict
    data_file2 = read_file(path_to_file2)  # dict
    diff = make_diff(data_file1, data_file2)
    return formatting(diff, format)
