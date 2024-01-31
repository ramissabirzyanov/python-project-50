def get_children(d):
    return d.get('children')


def get_key(d):
    return d.get('key')


def get_change(d):
    return d.get('change')


def get_value(d):
    if 'value' in d:
        return d.get('value')
    elif 'value1' in d:
        return d.get('value1')
    elif 'value2' in d:
        return d.get('value2')


def to_str(obj, depth):
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


def to_stylish(node, depth=1):
    result = []
    for item in node:
        indent = make_indent(depth)[0]
        closing_indent = make_indent(depth)[1]
        if 'children' in item:
            children = get_children(item)
            result_str = to_stylish(children, depth + 1)
            result.append(f"{indent}{'  '}{get_key(item)}: {result_str}")
        if get_change(item) == '+':
            result_str = f"{indent}{'+ '}{get_key(item)}: {to_str(get_value(item), depth + 1)}"
            result.append(result_str)
        elif get_change(item) == '-':
            result_str = f"{indent}{'- '}{get_key(item)}: {to_str(get_value(item), depth + 1)}"
            result.append(result_str)
        elif get_change(item) == ' ':
            result_str = f"{indent}{'  '}{get_key(item)}: {to_str(get_value(item), depth + 1)}"
            result.append(result_str)
        stylish = "\n".join(result)
    return f"{{\n{stylish}\n{closing_indent}}}"


def make_indent(depth, amount_spaces=4):
    indent = " " * (depth * amount_spaces - 2)
    closing_indent = " " * (depth * amount_spaces - 4)
    return indent, closing_indent
