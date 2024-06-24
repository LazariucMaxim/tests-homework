import pytest
from main import area_and_perimeter_of_square, area_and_perimeter_of_rectangle, quadratic_equation


@pytest.mark.parametrize(
    'a,expected',
    ([a, (a**2, 4*a)] for a in range(5))
)
def test_area_and_perimeter_of_square(a, expected):
    actual = area_and_perimeter_of_square(a)
    assert actual == expected


@pytest.mark.parametrize(
    'a,b,expected',
    ([a, b, (a*b, (a+b)*2)] for a, b in zip(range(5), range(4, 9)))
)
def test_area_and_perimeter_of_rectangle(a, b, expected):
    actual = area_and_perimeter_of_rectangle(a, b)
    assert actual == expected


@pytest.mark.parametrize(
    'a,b,c,expected',
    (
        [1, 2, 2, 'корней нет'],
        [4, 16, 16, -2],
        [1, -6, 5, (1, 5)]
    )
)
def test_quadratic_equation(a, b, c, expected):
    actual = quadratic_equation(a, b, c)
    assert actual == expected
