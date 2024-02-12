from gendiff import generate_diff


def test_gendiff_flat_json():
    diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'stylish')
    expected = open("tests/fixtures/expected_flat.txt").read()
    assert diff == expected


def test_gendiff_flat_yaml():
    diff = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", 'stylish')
    expected = open("tests/fixtures/expected_flat.txt").read()
    assert diff == expected
