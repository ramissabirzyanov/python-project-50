#INDENT = " "
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
    

def to_str(v, amount_indent=2):
    if isinstance(v, bool):
        return str(v).lower()
    elif v is None:
        return 'null'
    elif isinstance(v, int):
        return str(v)
    elif isinstance(v, dict):
        indent = " " * (8 + amount_indent)
        nodes = []
        for key, value in v.items():
            new_value =  to_str(value, amount_indent=6)
            nodes.append(f"{indent}{'  '}{key}: {new_value}")
        return "{\n" + "\n".join(nodes) + "\n" + f"{indent}" + "}"
    return v 

node = [{'key': 'common', 'children': [
    {'change': '+', 'key': 'follow', 'value': False}, 
    {'change': ' ', 'key': 'setting1', 'value': 'Value 1'}, 
    {'change': '-', 'key': 'setting2', 'value': 200}, 
    {'change': '-', 'key': 'setting3', 'value1': True}, 
    {'change': '+', 'key': 'setting3', 'value2': None}, 
    {'change': '+', 'key': 'setting4', 'value': 'blah blah'}, 
    {'change': '+', 'key': 'setting5', 'value': {'key5': 'value5'}}, 
    {'key': 'setting6', 'children': [
        {'key': 'doge', 'children': [
            {'change': '-', 'key': 'wow', 'value1': ''}, 
            {'change': '+', 'key': 'wow', 'value2': 'so much'}]}, 
            {'change': ' ', 'key': 'key', 'value': 'value'}, 
            {'change': '+', 'key': 'ops', 'value': 'vops'}]}]}]
def to_stylish(node, indent= "  "):
    result = []
    for item in node:
        if get_change(item) is None:
            result_str = f"{indent}{get_key(item)}:" + " {"
            result.append(result_str)
        elif get_change(item) == '+':
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
            indent = indent * 2
            result.append(to_stylish(children, indent) + "\n}")
    return "\n".join(result)
print(to_stylish(node))
      