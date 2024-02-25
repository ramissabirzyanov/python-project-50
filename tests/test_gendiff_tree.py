import pytest
from gendiff import generate_diff


@pytest.fixture(params=[('stylish', open("tests/fixtures/expected_stylish.txt").read()),
                        ('plain', open("tests/fixtures/expected_plain.txt").read()),
                        ('json', open("tests/fixtures/expected_json.json").read())])
def formats(request):
    return request.param


@pytest.fixture(params=[("tests/fixtures/tree1.json", "tests/fixtures/tree2.json"),
                        ("tests/fixtures/tree1.yaml", "tests/fixtures/tree2.yaml")])
def get_path(request):
    return request.param


def test_gendiff(get_path, formats):
    file1, file2 = get_path
    format, expected = formats
    assert generate_diff(file1, file2, format) == expected
