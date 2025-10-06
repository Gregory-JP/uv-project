"""Main module for greeting message.

This script prints a greeting message when executed.
"""

from my_package.my_module import my_function


def run() -> int:
    """Print a greeting message."""
    print("Hello, World!")
    return my_function(x=2, y=4)


if __name__ == "__main__":
    run()
