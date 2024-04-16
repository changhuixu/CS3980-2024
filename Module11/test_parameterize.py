import pytest


@pytest.mark.parametrize("input, expected", [("2+3", 5), ("7-9", -2)])
def test_para(input, expected):
    print(input)
    assert eval(input) == expected
