"""
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approach of summing 'Equally Spaced Abscissas'

method 2:
"Simpson Rule"

"""
import logging
logger = logging.getLogger(__name__)


def method_2(boundary: list[int], steps: int) -> float:
    logger.error(">>> Entering method_2(boundary=%s,steps=%s)", boundary, steps, extra={"event.action": "method_2", "logrite.boundary": boundary, "logrite.steps": steps})
    # "Simpson Rule"
    # int(f) = delta_x/2 * (b-a)/3*(f1 + 4f2 + 2f_3 + ... + fn)
    """
    Calculate the definite integral of a function using Simpson's Rule.
    :param boundary: A list containing the lower and upper bounds of integration.
    :param steps: The number of steps or resolution for the integration.
    :return: The approximate integral value.

    >>> round(method_2([0, 2, 4], 10), 10)
    2.6666666667
    >>> round(method_2([2, 0], 10), 10)
    -0.2666666667
    >>> round(method_2([-2, -1], 10), 10)
    2.172
    >>> round(method_2([0, 1], 10), 10)
    0.3333333333
    >>> round(method_2([0, 2], 10), 10)
    2.6666666667
    >>> round(method_2([0, 2], 100), 10)
    2.5621226667
    >>> round(method_2([0, 1], 1000), 10)
    0.3320026653
    >>> round(method_2([0, 2], 0), 10)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Number of steps must be greater than zero
    >>> round(method_2([0, 2], -10), 10)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Number of steps must be greater than zero
    """
    if steps <= 0:
        raise ZeroDivisionError("Number of steps must be greater than zero")

    h = (boundary[1] - boundary[0]) / steps
    logger.error("method_2(boundary=%s,steps=%s): h → %s", boundary, steps, h, extra={"event.action": "method_2", "logrite.boundary": boundary, "logrite.steps": steps})
    a = boundary[0]
    b = boundary[1]
    x_i = make_points(a, b, h)
    logger.error("method_2(boundary=%s,steps=%s): x_i → %s", boundary, steps, x_i, extra={"event.action": "method_2", "logrite.boundary": boundary, "logrite.steps": steps})
    y = 0.0
    y += (h / 3.0) * f(a)
    cnt = 2
    for i in x_i:
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i)
        cnt += 1
    y += (h / 3.0) * f(b)
    logger.warning("<<< Exiting method_2(boundary=%s,steps=%s)", boundary, steps, extra={"event.action": "method_2", "logrite.boundary": boundary, "logrite.steps": steps})
    return y


def make_points(a, b, h):
    logger.error(">>> Entering make_points(a=%s,b=%s,h=%s)", a, b, h, extra={"event.action": "make_points", "logrite.a": a, "logrite.b": b, "logrite.h": h})
    x = a + h
    while x < (b - h):
        yield x
        x = x + h
        logger.warning("<<< Exiting make_points(a=%s,b=%s,h=%s)", a, b, h, extra={"event.action": "make_points", "logrite.a": a, "logrite.b": b, "logrite.h": h})


def f(x):  # enter your function here
    logger.error(">>> Entering f(x=%s)", x, extra={"event.action": "f", "logrite.x": x})
    y = (x - 0) * (x - 0)
    logger.error("f(x=%s): y → %s", x, y, extra={"event.action": "f", "logrite.x": x})
    logger.warning("<<< Exiting f(x=%s)", x, extra={"event.action": "f", "logrite.x": x})
    return y


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    a = 0.0  # Lower bound of integration
    b = 1.0  # Upper bound of integration
    steps = 10.0  # number of steps or resolution
    boundary = [a, b]  # boundary of integration
    y = method_2(boundary, steps)
    logger.error("main(): y → %s", y, extra={"event.action": "main"})
    print(f"y = {y}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
