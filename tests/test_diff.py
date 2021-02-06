import os
import json
from gendiff.diff_generator import generate_diff


error_message = 'Diffs are not the same'
arguments = [
    ('./tests/fixtures/first_nested_file.json',
     './tests/fixtures/second_nested_file.yaml',
     './tests/fixtures/expected_json.json', 'json'),

    ('./tests/fixtures/first_nested_file.json',
     './tests/fixtures/second_nested_file.yaml',
     './tests/fixtures/expected_plain.txt', 'plain'),

    ('./tests/fixtures/first_nested_file.json',
     './tests/fixtures/second_nested_file.yaml',
     './tests/fixtures/expected_nested.txt', 'stylish'),
]


def test_generate_diff():
    for items in arguments:
        file1, file2, expected_file, output_format = items
        _, extention = os.path.splitext(expected_file)

        with open(expected_file, 'r') as input_file:
            expected = input_file.read()

        if extention == '.json':
            assert json.loads(expected) == json.loads(generate_diff(
                file1, file2, output_format
            )), error_message
        else:
            assert expected == generate_diff(
                file1, file2, output_format
            ), error_message
