"""
TASK:
Given a real number n, find the square root of n.
For example, given n = 9, return 3.
"""


def sqrt(n):
    """
    Returns the square root of a number n using the Newton's method.

    Parameters:
    n (float): The number to find the square root of.

    Returns:
    float: The square root of n.
    """

    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

    """
    Algorithm description:

    To solve the problem, we use the Newton's method for finding the root.
    The Newton's method involves iteratively approximating the root
    by computing the following value:

    x = 1/2 * (x + n / x)

    where x is the current approximation of the root, and n is the number
    for which we are trying to find the square root.

    Initially, we set x to n, since the square root of n lies somewhere
    between 0 and n. Then we compute y, which will be the initial
    approximation of the root, iteratively computing the next value until
    the difference between the current and previous value becomes small enough.

    The process is repeated until y < x. At the end, we return x
    as the result - this will be the square root of n.
    """
