from gendiff_package.gendiff import generate_diff


def test_gendiff_flat_json():
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json", format='stylish')
    expected = open("tests/fixtures/expected_flat.txt").read()
    assert diff == expected

def test_gendiff_flat_yaml():
    diff = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", format='stylish')
    expected = open("tests/fixtures/expected_flat.txt").read()
    assert diff == expected

def test_gendiff_tree_json():
    diff = generate_diff("tests/fixtures/tree1.json", "tests/fixtures/tree2.json", format='stylish')
    expected = open("tests/fixtures/expected_stylish.txt").read()
    assert diff == expected

def test_gendiff_tree_yaml():
    diff = generate_diff("tests/fixtures/tree1.yaml", "tests/fixtures/tree2.yaml", format='stylish')
    expected = open("tests/fixtures/expected_stylish.txt").read()
    assert diff == expected