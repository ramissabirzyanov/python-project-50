from gendiff_package.gendiff import generate_diff


def test_gendiff_json():
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    expected = open("tests/fixtures/expected_plain.txt").read()
    assert diff == expected

def test_gendiff_yaml():
    diff = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml")
    expected = open("tests/fixtures/expected_plain.txt").read()
    assert diff == expected

def test_gendiff_tree():
    diff = generate_diff("tests/fixtures/tree1.json", "tests/fixtures/tree2.json")
    expected = open("tests/fixtures/expected_tree.txt").read()
    assert diff == expected