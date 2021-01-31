import gendiff.gendiff as gd


def test_flat():
    with open('./tests/fixtures/expected_flat.txt', 'r') as input_file:
        expected = input_file.read()
    with open('./tests/fixtures/expected_nested.txt', 'r') as input_file:
        expected_nested = input_file.read()
    assert expected == gd.generate_diff(
        './tests/fixtures/first_file.json',
        './tests/fixtures/second_file.json',
        'stylish'
    ), "Flat diffs are not the same"
    assert expected == gd.generate_diff(
        './tests/fixtures/first_file.yaml',
        './tests/fixtures/second_file.yaml',
        'stylish'
    ), "Flat diffs are not the same"
    assert expected_nested == gd.generate_diff(
        './tests/fixtures/first_nested_file.json',
        './tests/fixtures/second_nested_file.json',
        'stylish'
    ), "Flat diffs are not the same"
    assert expected_nested == gd.generate_diff(
        './tests/fixtures/first_nested_file.yaml',
        './tests/fixtures/second_nested_file.yaml',
        'stylish'
    ), "Flat diffs are not the same"
