"""Module for environment variable testing and simple addition function.

This module loads environment variables using dotenv, provides a function
to add two integers, and demonstrates usage when run as a script.
"""


def my_function(x: int, y: int) -> int:
    """Add two integers and return the result.

    Parameters
    ----------
    x : int
        First integer to add.
    y : int
        Second integer to add.

    Returns
    -------
    int
        The sum of x and y.

    """
    return x + y


def run_from_script() -> str:
    """Test environment variables and demonstrate the addition function.

    Prints the value of the GREETINGS environment variable
    and the result of my_function(1, 2).
    """
    # Seguindo a programação normal
    my_result = my_function(1, 2)
    return f"The result is {my_result}"


if __name__ == "__main__":
    run_from_script()
