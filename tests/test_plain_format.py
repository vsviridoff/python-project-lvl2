import gendiff.gendiff as gd


def test_plain():
    with open('./tests/fixtures/expected_plain.txt', 'r') as input_file:
        expected = input_file.read()
        assert expected == gd.generate_diff(
            './tests/fixtures/first_nested_file.json',
            './tests/fixtures/second_nested_file.json',
            'plain'
        ), 'Flat diffs are not the same'
        assert expected == gd.generate_diff(
            './tests/fixtures/first_nested_file.yaml',
            './tests/fixtures/second_nested_file.yaml',
            'plain'
        ), 'Flat diffs are not the same' 
