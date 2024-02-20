from gendiff.formatters.stylish_format import to_str


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
        new_path = f"{path}.{item.get('key')}"
        value = item.get('value')
        change = item.get('change')
        if change == '+':
            result_str = (f"Property '{new_path[1:]}' was added with value: "
                          f"{to_complex_value_or_str(value)}")
            result.append(result_str)
        elif change == '-':
            result_str = f"Property '{new_path[1:]}' was removed"
            result.append(result_str)
        elif change == '-/+':
            result_str = (f"Property '{new_path[1:]}' was updated."
                          f" From {to_complex_value_or_str(value[0])}"
                          f" to {to_complex_value_or_str(value[1])}")
            result.append(result_str)
        if 'children' in item:
            children = item.get('children')
            result_str = to_plain(children, new_path)
            result.append(f"{result_str}")
    return "\n".join(result)
