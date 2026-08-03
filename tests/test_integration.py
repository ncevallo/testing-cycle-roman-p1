# Integration tests. Combine two or more units and verify that they work as a
# group. Section 7 of the specification requires that the result of add_roman
# and subtract_roman is always accepted by is_valid_roman, and that the
# operations are consistent with to_roman and from_roman.
from roman.converter import (
    add_roman,
    subtract_roman,
    is_valid_roman,
    from_roman,
)


def test_add_result_is_canonical_and_valid():
    # from_roman("II") + from_roman("II") == 4, and to_roman(4) must be "IV".
    # The result must also be accepted by is_valid_roman (section 7).
    result = add_roman("II", "II")
    assert result == "IV"
    assert is_valid_roman(result)


def test_add_roundtrip_consistency():
    # add_roman must agree with from_roman applied to its own result.
    result = add_roman("IV", "VI")
    assert from_roman(result) == from_roman("IV") + from_roman("VI")
    assert is_valid_roman(result)


def test_subtract_result_is_valid():
    result = subtract_roman("X", "I")
    assert result == "IX"
    assert is_valid_roman(result)
