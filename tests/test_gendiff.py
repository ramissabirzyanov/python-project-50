import pytest
from gendiff import generate_diff


@pytest.fixture(params=[
    ('stylish', open("tests/fixtures/expected_stylish.txt").read()),
    ('plain', open("tests/fixtures/expected_plain.txt").read()),
    ('json', open("tests/fixtures/expected_json.txt").read()),
    ])
def formats(request):
    return request.param
    

@pytest.fixture
def paths_of_trees():
    return ("tests/fixtures/tree1.json", "tests/fixtures/tree2.json")


def test_gendiff(paths_of_trees, formats):
    format, expected = formats
    assert generate_diff(paths_of_trees[0], paths_of_trees[1], format) == expected
