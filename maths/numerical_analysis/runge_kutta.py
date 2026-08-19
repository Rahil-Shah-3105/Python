import numpy as np
import logging
logger = logging.getLogger(__name__)


def runge_kutta(f, y0, x0, h, x_end):
    """
    Calculate the numeric solution at each step to the ODE f(x, y) using RK4

    https://en.wikipedia.org/wiki/Runge-Kutta_methods

    Arguments:
    f -- The ode as a function of x and y
    y0 -- the initial value for y
    x0 -- the initial value for x
    h -- the stepsize
    x_end -- the end value for x

    >>> # the exact solution is math.exp(x)
    >>> def f(x, y):
    ...     return y
    >>> y0 = 1
    >>> y = runge_kutta(f, y0, 0.0, 0.01, 5)
    >>> float(y[-1])
    148.41315904125113
    """
    logger.debug(">>> Entering runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s)", f, y0, x0, h, x_end)
    n = int(np.ceil((x_end - x0) / h))
    logger.debug("runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s): n → %s", f, y0, x0, h, x_end, n)
    y = np.zeros((n + 1,))
    logger.debug("runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s): y → %s", f, y0, x0, h, x_end, y)
    y[0] = y0
    x = x0

    for k in range(n):
        k1 = f(x, y[k])
        logger.debug("runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s): k1 → %s", f, y0, x0, h, x_end, k1)
        k2 = f(x + 0.5 * h, y[k] + 0.5 * h * k1)
        logger.debug("runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s): k2 → %s", f, y0, x0, h, x_end, k2)
        k3 = f(x + 0.5 * h, y[k] + 0.5 * h * k2)
        logger.debug("runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s): k3 → %s", f, y0, x0, h, x_end, k3)
        k4 = f(x + h, y[k] + h * k3)
        logger.debug("runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s): k4 → %s", f, y0, x0, h, x_end, k4)
        y[k + 1] = y[k] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h

    logger.debug("<<< Exiting runge_kutta(f=%s,y0=%s,x0=%s,h=%s,x_end=%s)", f, y0, x0, h, x_end)
    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
