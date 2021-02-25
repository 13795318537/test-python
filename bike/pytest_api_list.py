import pytest
from pytest import approx

nums = 0.1 + 0.2
print(nums)
assert nums == approx(0.3)

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), pytest.param("6*9", 42, marks=pytest.mark.xfail),],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected