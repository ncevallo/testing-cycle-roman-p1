# Unit tests (structural / white-box) for to_roman and companion functions.
# Derived from the source code, targeting the branches identified in the CFG
# of src/roman/converter.py.
import pytest
from roman.converter import (
    to_roman,
    from_roman,
    is_valid_roman,
    add_roman,
    subtract_roman,
    RomanError,
)


# ---------- to_roman: type and range guards ----------

def test_to_roman_rejects_string():
    with pytest.raises(RomanError):
        to_roman("5")


def test_to_roman_rejects_float():
    with pytest.raises(RomanError):
        to_roman(5.0)


def test_to_roman_rejects_bool_true():
    with pytest.raises(RomanError):
        to_roman(True)


def test_to_roman_rejects_bool_false():
    with pytest.raises(RomanError):
        to_roman(False)


def test_to_roman_rejects_zero():
    with pytest.raises(RomanError):
        to_roman(0)


def test_to_roman_rejects_negative():
    with pytest.raises(RomanError):
        to_roman(-1)


def test_to_roman_rejects_above_max():
    with pytest.raises(RomanError):
        to_roman(4000)


# ---------- to_roman: loop coverage (each pair in _PAIRS at least once) ----------

def test_to_roman_boundary_min():
    assert to_roman(1) == "I"


def test_to_roman_boundary_max():
    # Exercises multiple loop iterations; canonical value assertions live in
    # acceptance tests (functional, derived from the specification).
    assert to_roman(3999) == "MMMCMXCIX"


def test_to_roman_exercises_ten():
    # Covers the (10, "X") pair in the _PAIRS loop.
    assert to_roman(10) == "X"


def test_to_roman_exercises_fifty():
    assert to_roman(50) == "L"


def test_to_roman_exercises_hundred():
    assert to_roman(100) == "C"


def test_to_roman_exercises_five_hundred():
    assert to_roman(500) == "D"


# ---------- from_roman: guards ----------

def test_from_roman_rejects_non_string():
    with pytest.raises(RomanError):
        from_roman(5)


def test_from_roman_rejects_empty():
    with pytest.raises(RomanError):
        from_roman("")


def test_from_roman_rejects_unknown_character():
    with pytest.raises(RomanError):
        from_roman("Z")


def test_from_roman_rejects_out_of_range():
    with pytest.raises(RomanError):
        from_roman("MMMM")


def test_from_roman_rejects_invalid_subtractive_pair():
    with pytest.raises(RomanError):
        from_roman("IL")


# ---------- from_roman: valid subtractive pairs (branch 72-74) ----------

def test_from_roman_IV():
    assert from_roman("IV") == 4


def test_from_roman_IX():
    assert from_roman("IX") == 9


def test_from_roman_XL():
    assert from_roman("XL") == 40


def test_from_roman_XC():
    assert from_roman("XC") == 90


def test_from_roman_CD():
    assert from_roman("CD") == 400


def test_from_roman_CM():
    assert from_roman("CM") == 900


def test_from_roman_MCMXCIV():
    assert from_roman("MCMXCIV") == 1994


# ---------- is_valid_roman ----------

def test_is_valid_true_for_canonical():
    assert is_valid_roman("IV") is True


def test_is_valid_false_for_unknown_character():
    assert is_valid_roman("Z") is False


def test_is_valid_false_for_empty():
    assert is_valid_roman("") is False


# ---------- add_roman / subtract_roman ----------

def test_add_roman_simple():
    assert add_roman("V", "V") == "X"


def test_subtract_roman_simple():
    assert subtract_roman("X", "I") == "IX"
