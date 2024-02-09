def get_children(d):
    return d.get('children')


def get_key(d):
    return d.get('key')


def get_change(d):
    return d.get('change')


def get_value(d):
    return d.get('value')


def make_indent(depth, amount_spaces=4):
    indent = " " * (depth * amount_spaces - 2)
    closing_indent = " " * (depth * amount_spaces - 4)
    return indent, closing_indent


def to_str(obj, depth=1):
    if isinstance(obj, bool):
        return str(obj).lower()
    elif obj is None:
        return 'null'
    elif isinstance(obj, int):
        return str(obj)
    elif isinstance(obj, dict):
        nodes = []
        for key, value in obj.items():
            indent = make_indent(depth)[0]
            close_indent = make_indent(depth)[1]
            nodes.append(f"{indent}{'  '}{key}: {to_str(value, depth + 1)}")
            result = "\n".join(nodes)
        return f"{{\n{result}\n{close_indent}}}"
    return obj


CHANGES = {'+': '+ ',
           '-': '- ',
           ' ': '  ',
           '-/+': ('- ', '+ ')
           }


def to_stylish(node, depth=1):
    result = []
    for item in node:
        indent = make_indent(depth)[0]
        closing_indent = make_indent(depth)[1]
        change = get_change(item)
        key = get_key(item)
        value = get_value(item)
        if change in CHANGES:
            if change == '-/+':
                result_str1 = (f"{indent}{CHANGES.get(change)[0]}{key}: "
                              f"{to_str(value[0], depth + 1)}")
                result_str2 = (f"{indent}{CHANGES.get(change)[1]}{key}: "
                               f"{to_str(value[1], depth + 1)}")
                result.append(result_str1)
                result.append(result_str2)
            else:
                result_str = (f"{indent}{CHANGES.get(change)}{key}: "
                              f"{to_str(value, depth + 1)}")
                result.append(result_str)
        if 'children' in item:
            children = get_children(item)
            result_str = to_stylish(children, depth + 1)
            result.append(f"{indent}{'  '}{key}: {result_str}")
        stylish = "\n".join(result)
    return f"{{\n{stylish}\n{closing_indent}}}"
