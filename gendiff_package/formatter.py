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

def to_str(obj, amount_indent=4):
    if isinstance(obj, bool):
        return str(obj).lower()
    elif obj is None:
        return 'null'
    elif isinstance(obj, int):
        return str(obj)
    elif isinstance(obj, dict):
        nodes = []
        for key, value in obj.items():
            new_value =  to_str(value, amount_indent + 4)
            indent = " " * (amount_indent + 4)
            close_indent = " " * (amount_indent)
            nodes.append(f"{indent}{key}: {new_value}")
            result = "\n".join(nodes)
        return f"{{\n{result}\n{close_indent}}}"            
    return obj

def to_stylish(node, amount_indent=2):
    indent = " " * (amount_indent)
    closing_indent = " " * (amount_indent - 2)
    result = []
    for item in node:
        if get_change(item) == '+':
            result_str = f"{indent}{'+ '}{get_key(item)}: {to_str(get_value(item))}"
            result.append(result_str)
        elif get_change(item) == '-':
            result_str = f"{indent}{'- '}{get_key(item)}: {to_str(get_value(item))}"
            result.append(result_str)
        elif get_change(item) == ' ':
            result_str = f"{indent}{'  '}{get_key(item)}: {to_str(get_value(item))}"
            result.append(result_str)
        if 'children' in item:
            children = get_children(item)
            result_str = (to_stylish(children, amount_indent + 4))
            result.append(f"{indent}{'  '}{get_key(item)}: {result_str}")
        stylish = "\n".join(result)
    return f"{{\n{stylish}\n{closing_indent}}}"

def make_indent(depth=1, amount_spaces=4):
    indent = " " * (depth*amount_spaces - 2)
    return indent
      