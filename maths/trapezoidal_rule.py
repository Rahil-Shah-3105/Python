import logging
logger = logging.getLogger(__name__)
"""
Numerical integration or quadrature for a smooth function f with known values at x_i
"""


def trapezoidal_rule(boundary, steps):
    """
    Implements the extended trapezoidal rule for numerical integration.
    The function f(x) is provided below.

    :param boundary: List containing the lower and upper bounds of integration [a, b]
    :param steps: The number of steps (intervals) used in the approximation
    :return: The numerical approximation of the integral

    >>> abs(trapezoidal_rule([0, 1], 10) - 0.33333) < 0.01
    True
    >>> abs(trapezoidal_rule([0, 1], 100) - 0.33333) < 0.01
    True
    >>> abs(trapezoidal_rule([0, 2], 1000) - 2.66667) < 0.01
    True
    >>> abs(trapezoidal_rule([1, 2], 1000) - 2.33333) < 0.01
    True
    """
    logger.debug(">>> Entering trapezoidal_rule(boundary=%s,steps=%s)", boundary, steps)
    h = (boundary[1] - boundary[0]) / steps
    logger.debug("trapezoidal_rule(boundary=%s,steps=%s): h → %s", boundary, steps, h)
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    logger.debug("trapezoidal_rule(boundary=%s,steps=%s): x_i → %s", boundary, steps, x_i)
    y = 0.0
    y += (h / 2.0) * f(a)
    for i in x_i:
        y += h * f(i)
    y += (h / 2.0) * f(b)
    logger.debug("<<< Exiting trapezoidal_rule(boundary=%s,steps=%s)", boundary, steps)
    return y


def make_points(a, b, h):
    """
    Generates points between a and b with step size h for trapezoidal integration.

    :param a: The lower bound of integration
    :param b: The upper bound of integration
    :param h: The step size
    :yield: The next x-value in the range (a, b)

    >>> list(make_points(0, 1, 0.1))    # doctest: +NORMALIZE_WHITESPACE
    [0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, \
    0.8999999999999999]
    >>> list(make_points(0, 10, 2.5))
    [2.5, 5.0, 7.5]
    >>> list(make_points(0, 10, 2))
    [2, 4, 6, 8]
    >>> list(make_points(1, 21, 5))
    [6, 11, 16]
    >>> list(make_points(1, 5, 2))
    [3]
    >>> list(make_points(1, 4, 3))
    []
    """
    logger.debug(">>> Entering make_points(a=%s,b=%s,h=%s)", a, b, h)
    x = a + h
    while x <= (b - h):
        yield x
        x += h
        logger.debug("<<< Exiting make_points(a=%s,b=%s,h=%s)", a, b, h)


def f(x):
    """
    This is the function to integrate, f(x) = (x - 0)^2 = x^2.

    :param x: The input value
    :return: The value of f(x)

    >>> f(0)
    0
    >>> f(1)
    1
    >>> f(0.5)
    0.25
    """
    logger.debug(">>> Entering f(x=%s)", x)
    logger.debug("<<< Exiting f(x=%s)", x)
    return x**2


def main():
    """
    Main function to test the trapezoidal rule.
    :a: Lower bound of integration
    :b: Upper bound of integration
    :steps: define number of steps or resolution
    :boundary: define boundary of integration

    >>> main()
    y = 0.3349999999999999
    """
    logger.debug(">>> Entering main()")
    a = 0.0
    b = 1.0
    steps = 10.0
    logger.debug("main(): steps → %s", steps)
    boundary = [a, b]
    logger.debug("main(): boundary → %s", boundary)
    y = trapezoidal_rule(boundary, steps)
    logger.debug("main(): y → %s", y)
    print(f"y = {y}")
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
