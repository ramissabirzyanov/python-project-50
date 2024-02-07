from gendiff_package.formatters.stylish import get_change, get_children, get_key, get_value, to_str


def to_complex_value_or_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return to_str(value)


def to_plain(node, path=''):
    result = []
    for item in node:
        new_path = f"{path}.{get_key(item)}"
        if get_change(item) == '+':
            result_str = (f"Property '{new_path[1:]}'"
                          f" was added with value: {to_complex_value_or_str(get_value(item))}")
            result.append(result_str)
        elif get_change(item) == '-':
            result_str = f"Property '{new_path[1:]}' was removed"
            result.append(result_str)
        elif get_change(item) == '-/+':
            result_str = (f"Property '{new_path[1:]}' was updated."
                          f" From {to_complex_value_or_str(get_value(item)[0])}"
                          f" to {to_complex_value_or_str(get_value(item)[1])}")
            result.append(result_str)
        if 'children' in item:
            children = get_children(item)
            result_str = to_plain(children, new_path)
            result.append(f"{result_str}")
    return "\n".join(result)
