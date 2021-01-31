import gendiff.gendiff as gd
import json


def test_flat():
    with open('./tests/fixtures/expected_file.json') as input_file:
        expected = json.load(input_file)
        assert expected == json.loads(gd.generate_diff(
            './tests/fixtures/first_nested_file.json',
            './tests/fixtures/second_nested_file.json',
            'json'
        )), 'Json diffs are not the same'
