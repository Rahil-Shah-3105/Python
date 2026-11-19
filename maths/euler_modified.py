from collections.abc import Callable

import numpy as np
import logging
logger = logging.getLogger(__name__)


def euler_modified(
    ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float
) -> np.ndarray:
    logger.error(">>> Entering euler_modified(ode_func=%s,y0=%s,x0=%s,step_size=%s,x_end=%s)", ode_func, y0, x0, step_size, x_end, extra={"event.action": "euler_modified", "logrite.ode_func": ode_func, "logrite.y0": y0, "logrite.x0": x0, "logrite.step_size": step_size, "logrite.x_end": x_end})
    """
    Calculate solution at each step to an ODE using Euler's Modified Method
    The Euler Method is straightforward to implement, but can't give accurate solutions.
    So, some changes were proposed to improve accuracy.

    https://en.wikipedia.org/wiki/Euler_method

    Arguments:
    ode_func -- The ode as a function of x and y
    y0 -- the initial value for y
    x0 -- the initial value for x
    stepsize -- the increment value for x
    x_end -- the end value for x

    >>> # the exact solution is math.exp(x)
    >>> def f1(x, y):
    ...     return -2*x*(y**2)
    >>> y = euler_modified(f1, 1.0, 0.0, 0.2, 1.0)
    >>> float(y[-1])
    0.503338255442106
    >>> import math
    >>> def f2(x, y):
    ...     return -2*y + (x**3)*math.exp(-2*x)
    >>> y = euler_modified(f2, 1.0, 0.0, 0.1, 0.3)
    >>> float(y[-1])
    0.5525976431951775
    """
    n = int(np.ceil((x_end - x0) / step_size))
    logger.error("euler_modified(ode_func=%s,y0=%s,x0=%s,step_size=%s,x_end=%s): n → %s", ode_func, y0, x0, step_size, x_end, n, extra={"event.action": "euler_modified", "logrite.ode_func": ode_func, "logrite.y0": y0, "logrite.x0": x0, "logrite.step_size": step_size, "logrite.x_end": x_end})
    y = np.zeros((n + 1,))
    logger.error("euler_modified(ode_func=%s,y0=%s,x0=%s,step_size=%s,x_end=%s): y → %s", ode_func, y0, x0, step_size, x_end, y, extra={"event.action": "euler_modified", "logrite.ode_func": ode_func, "logrite.y0": y0, "logrite.x0": x0, "logrite.step_size": step_size, "logrite.x_end": x_end})
    y[0] = y0
    x = x0

    for k in range(n):
        y_get = y[k] + step_size * ode_func(x, y[k])
        logger.error("euler_modified(ode_func=%s,y0=%s,x0=%s,step_size=%s,x_end=%s): y_get → %s", ode_func, y0, x0, step_size, x_end, y_get, extra={"event.action": "euler_modified", "logrite.ode_func": ode_func, "logrite.y0": y0, "logrite.x0": x0, "logrite.step_size": step_size, "logrite.x_end": x_end})
        y[k + 1] = y[k] + (
            (step_size / 2) * (ode_func(x, y[k]) + ode_func(x + step_size, y_get))
        )
        x += step_size

    logger.warning("<<< Exiting euler_modified(ode_func=%s,y0=%s,x0=%s,step_size=%s,x_end=%s)", ode_func, y0, x0, step_size, x_end, extra={"event.action": "euler_modified", "logrite.ode_func": ode_func, "logrite.y0": y0, "logrite.x0": x0, "logrite.step_size": step_size, "logrite.x_end": x_end})
    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
