"""Tests for the main module."""

from my_package.my_module import my_function

EXPECTED_SUM_RESULT = 6


def test_main_returns_hello_world():
    """Tests if the main function returns the correct string."""
    result = my_function(2, 4)
    assert result == EXPECTED_SUM_RESULT
