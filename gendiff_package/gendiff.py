import json


def bool_to_str(dict):
    for k, v in dict.items():
        if v is True:
            dict[k] = 'true'
        elif v is False:
            dict[k] = 'false'
        elif v is None:
            dict[k] = 'null'
    return dict


def generate_diff(path_to_file1, path_to_file2):
    with open(path_to_file1, "r") as file1:
        with open(path_to_file2, "r") as file2:
            data_file1 = json.load(file1)  # dict
            data_file2 = json.load(file2)  # dict
            diff = {}
            for key1 in sorted(data_file1):
                if key1 in data_file2:
                    if data_file1[key1] == data_file2[key1]:
                        diff['    ' + key1] = data_file1[key1]
                    else:
                        diff['  - ' + key1] = data_file1[key1]
                        diff['  + ' + key1] = data_file2[key1]
                else:
                    diff['  - ' + key1] = data_file1[key1]
            for key2 in sorted(data_file2):
                if key2 not in data_file1:
                    diff['  + ' + key2] = data_file2[key2]
            diff = bool_to_str(diff)
            return ("{\n"
                    + "\n".join([f'{key}: {value}' for key, value in diff.items()])
                    + "\n}")
