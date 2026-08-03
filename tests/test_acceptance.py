# Acceptance tests (functional / black-box). Each test is a Given / When / Then
# criterion taken directly from the functional specification (SPECIFICATION.md).
# These tests do not look at the source code, only at the observable behaviour
# the specification requires.
import pytest
from roman.converter import to_roman, from_roman, is_valid_roman, RomanError


# ---------------------------------------------------------------------------
# Criterion 1 - Section 2: mandatory canonical value for 1994.
# Given a valid integer in the supported range,
# When to_roman(1994) is called,
# Then it returns the canonical roman string "MCMXCIV".
# ---------------------------------------------------------------------------
def test_acceptance_to_roman_1994_is_canonical():
    assert to_roman(1994) == "MCMXCIV"


# ---------------------------------------------------------------------------
# Criterion 2 - Section 3: leading and trailing whitespace is tolerated.
# Given a roman string with stray blanks on the ends,
# When from_roman("  IV  ") is called,
# Then it returns 4 (the ends are trimmed before processing).
# ---------------------------------------------------------------------------
def test_acceptance_from_roman_trims_ends():
    assert from_roman("  IV  ") == 4


# ---------------------------------------------------------------------------
# Criterion 3 - Section 4: only canonical form is accepted.
# Given a roman string that represents a value but is not in canonical form,
# When from_roman("IIII") is called (canonical form of 4 is IV),
# Then RomanError is raised.
# ---------------------------------------------------------------------------
def test_acceptance_from_roman_rejects_non_canonical_IIII():
    with pytest.raises(RomanError):
        from_roman("IIII")


# Same criterion applied through is_valid_roman: non-canonical must be False.
def test_acceptance_is_valid_rejects_non_canonical():
    assert is_valid_roman("IIII") is False
