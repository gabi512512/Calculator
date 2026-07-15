import pytest
from calculator import Calculator
from constants import INPUT_ERROR

@pytest.fixture
def calc():
    return Calculator()

# --- getNumber ---

@pytest.mark.parametrize("text, expected", [
    ("5", 5),
    ("-5", -5),
    ("0", 0),
    ("  5  ", 5),
    ("5.5", 5.5),
])
def test_get_number_valid(calc, text, expected):
    assert calc.getNumber(text) == expected


@pytest.mark.parametrize("text", [
    "5@",
    "",
    " ",
    "@",
    "abc",
])
def test_get_number_invalid(calc, text):
    assert calc.getNumber(text) == INPUT_ERROR[0]

# --- add ---

@pytest.mark.parametrize("stored_result, number, expected", [
    (0, 5, 5),
    (5, 5, 10),
    (-5, 5, 0),
    (-10, 5, -5),
    (10, -5, 5),
])
def test_add(calc, stored_result, number, expected):
    calc.result = stored_result
    calc.add(number)
    assert calc.result == expected

# --- subtract ---

@pytest.mark.parametrize("stored_result, number, expected", [
    (10, 5, 5),
    (0, 5, -5),
    (5, 10, -5),
    (-5, -5, 0),
    (10, -5, 15),
])
def test_subtract(calc, stored_result, number, expected):
    calc.result = stored_result
    calc.subtract(number)
    assert calc.result == expected

# --- multiply ---

@pytest.mark.parametrize("stored_result, number, expected", [
    (0, 5, 0),
    (1, 5, 5),
    (5, 1, 5),
    (5, 5, 25),
    (5, -5, -25),
    (-5, 5, -25),
    (-5, -5, 25),
    (-0, 5, 0),
    (0, -5, 0),
    (5, -1, -5),
])
def test_multiply(calc, stored_result, number, expected):
    calc.result = stored_result
    calc.multiply(number)
    assert calc.result == expected

# --- divide ---

@pytest.mark.parametrize("stored_result, number, expected", [
    (0, 0, INPUT_ERROR[1]),
    (1, 0, INPUT_ERROR[1]),
    (5, 0, INPUT_ERROR[1]),
    (0, 1, 0),
    (0, 5, 0),
    (5, 1, 5),
    (5, 5, 1),
    (25, 5, 5),
    (-5, 5, -1),
    (5, -5, -1),
])
def test_divide(calc, stored_result, number, expected):
    calc.result = stored_result
    val_return = calc.divide(number)
    if number == 0:
        assert val_return == expected
    else:
        assert calc.result == expected

# --- clear ---

@pytest.mark.parametrize("stored_result", [
    0.0,
    5,
    -5,
    0,
    1,
])
def test_clear(calc, stored_result):
    calc.result = stored_result
    calc.clear()
    assert calc.result == 0.0