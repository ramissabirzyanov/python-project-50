from gendiff_package.gendiff import generate_diff


def test_gendiff_json():
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    excepted = open("tests/fixtures/expexted_json.txt").read()
    assert diff == excepted