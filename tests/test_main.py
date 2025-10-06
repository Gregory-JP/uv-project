"""Tests for the main module."""

from environments_config.__main__ import main


def test_main_returns_hello_world():
    """Tests if the main function returns the correct string."""
    assert main() == "Your project is set up correctly!"
