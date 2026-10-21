import math

import pytest

from factorial import factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 120),
        (10, 3628800),
        (20, 2432902008176640000),
    ],
)
def test_known_values(n, expected):
    assert factorial(n) == expected


def test_matches_math_factorial():
    for n in range(0, 60):
        assert factorial(n) == math.factorial(n)


def test_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("bad", [3.5, "5", None, True])
def test_non_integer_raises_type_error(bad):
    with pytest.raises(TypeError):
        factorial(bad)