import gendiff.gendiff as gd


ERROR_MASAGE = "Flat diffs are not the same"


def test_flat():
    with open('./tests/fixtures/expexted_flat.txt', 'r') as input_file:
        expected = input_file.read()
    assert expected == gd.generate_diff(
        './tests/fixtures/first_file.json',
        './tests/fixtures/second_file.json'
    ), ERROR_MASAGE
    assert expected == gd.generate_diff(
        './tests/fixtures/first_file.yaml',
        './tests/fixtures/second_file.yaml'
    ), ERROR_MASAGE
