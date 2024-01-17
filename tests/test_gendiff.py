from gendiff_package.gendiff import generate_diff


def test_gendiff_json():
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    excepted = open("tests/fixtures/expected_plain.txt").read()
    assert diff == excepted

def test_gendiff_yaml():
    diff = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml")
    excepted = open("tests/fixtures/expected_plain.txt").read()
    assert diff == excepted
