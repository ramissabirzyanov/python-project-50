from gendiff_package.parsing import read_file
from gendiff_package.formatters.stylish import to_stylish
from gendiff_package.formatters.plain import to_plain
from gendiff_package.formatters.json_format import to_json


def make_diff(data_file1, data_file2):
    nodes = []
    keys = data_file1.keys() | data_file2.keys()  # set
    for key in sorted(keys):
        if key not in data_file1:
            nodes.append({"change": "+",
                          "key": key,
                          "value": data_file2[key]})
        elif key not in data_file2:
            nodes.append({"change": "-",
                          "key": key,
                          "value": data_file1[key]})
        elif isinstance(data_file1[key], dict) and isinstance(data_file2[key], dict):
            nodes.append({"key": key,
                          "children": make_diff(data_file1[key], data_file2[key])})
        elif data_file1[key] == data_file2[key]:
            nodes.append({"change": " ",
                          "key": key,
                          "value": data_file1[key]})
        else:
            nodes.append({"change": "-/+",
                          "key": key,
                          "value": (data_file1[key], data_file2[key])})
    return nodes


def generate_diff(path_to_file1, path_to_file2, format):
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
