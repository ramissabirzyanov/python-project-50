from gendiff import generate_diff


def test_gendiff_tree_json():
    diff = generate_diff("tests/fixtures/tree1.json", "tests/fixtures/tree2.json", 'json')
    expected = open("tests/fixtures/expected_json.txt").read()
    assert diff == expected