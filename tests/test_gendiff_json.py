from gendiff.generate_diff import generate_diff


def test_gendiff_tree_json():
    diff = generate_diff("tests/fixtures/tree1.json", "tests/fixtures/tree2.json", format='json')
    expected = open("tests/fixtures/expected_json.txt").read()
    assert diff == expected
