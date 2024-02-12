import pytest
import os
from gendiff import generate_diff


@pytest.fixture(params=[
    ('stylish', open("tests/fixtures/expected_stylish.txt").read()),
    ('plain', open("tests/fixtures/expected_plain.txt").read()),
    ('json', open("tests/fixtures/expected_json.txt").read()),
    ])
def formats(request):
    return request.param
    

@pytest.fixture
def get_path():
    return ("tests/fixtures/tree1.json", "tests/fixtures/tree2.json")


def test_gendiff(get_path, formats):
    file1 = get_path[0]
    file2 = get_path[1]
    format, expected = formats
    assert generate_diff(file1, file2, format) == expected
