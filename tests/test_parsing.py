from gendiff.parsing import read_file


def test_read_file():
    file = read_file("tests/fixtures/file1.json")
    expected = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    }
    assert file == expected
    