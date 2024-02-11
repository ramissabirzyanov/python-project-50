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
