import gendiff.gendiff as gd


def test_flat():
    with open('./tests/fixtures/expexted_flat.txt', 'r') as input_file:
        expected = input_file.read()
    assert expected == gd.create_diff(
        './tests/fixtures/first_file.json',
        './tests/fixtures/second_file.json'
    ), "Flat diffs are not the same"
