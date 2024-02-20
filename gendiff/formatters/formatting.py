from gendiff.formatters.stylish_format import to_stylish
from gendiff.formatters.plain_format import to_plain
from gendiff.formatters.json_format import to_json


def formatting(tree, format):
    if format == 'stylish':
        return to_stylish(tree)
    elif format == 'plain':
        return to_plain(tree)
    elif format == 'json':
        return to_json(tree)
    else:
        raise NameError("unsupported format")
