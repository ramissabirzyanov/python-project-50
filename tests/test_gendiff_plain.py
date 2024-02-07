from gendiff_package.gendiff import generate_diff


def test_gendiff_tree_json():
    diff = generate_diff("tests/fixtures/tree1.json", "tests/fixtures/tree2.json", format='plain')
    expected = open("tests/fixtures/expected_plain.txt").read()
    assert diff == expected

def test_gendiff_tree_yaml():
    diff = generate_diff("tests/fixtures/tree1.yaml", "tests/fixtures/tree2.yaml", format='plain')
    expected = open("tests/fixtures/expected_plain.txt").read()
    assert diff == expected