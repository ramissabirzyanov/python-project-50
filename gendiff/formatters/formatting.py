from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json_format import to_json


def set_format(tree, format):
    if format == 'stylish':
        return to_stylish(tree)
    elif format == 'plain':
        return to_plain(tree)
    elif format == 'json':
        return to_json(tree)
    else:
        raise NameError("unsupported format")
