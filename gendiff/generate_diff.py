from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json_format import to_json
from gendiff.parsing import read_file
from gendiff.make_diff import make_diff


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    data_file1 = read_file(path_to_file1)  # dict
    data_file2 = read_file(path_to_file2)  # dict
    diff = make_diff(data_file1, data_file2)
    if format == 'stylish':
        return to_stylish(diff)
    elif format == 'plain':
        return to_plain(diff)
    elif format == 'json':
        return to_json(diff)
    else:
        raise NameError("unsupported format")
