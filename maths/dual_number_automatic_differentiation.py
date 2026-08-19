from math import factorial
import logging
logger = logging.getLogger(__name__)

"""
https://en.wikipedia.org/wiki/Automatic_differentiation#Automatic_differentiation_using_dual_numbers
https://blog.jliszka.org/2013/10/24/exact-numeric-nth-derivatives.html

Note this only works for basic functions, f(x) where the power of x is positive.
"""


class Dual:
    def __init__(self, real, rank):
        logger.debug(">>> Entering __init__(real=%s,rank=%s)", real, rank)
        self.real = real
        logger.debug("__init__(self=%s,real=%s,rank=%s): self.real → %s", self, real, rank, self.real)
        if isinstance(rank, int):
            self.duals = [1] * rank
            logger.debug("__init__(self=%s,real=%s,rank=%s): self.duals → %s", self, real, rank, self.duals)
        else:
            logger.debug("<<< Exiting __init__(real=%s,rank=%s)", real, rank)
            self.duals = rank

    def __repr__(self):
        logger.debug(">>> Entering __repr__()")
        s = "+".join(f"{dual}E{n}" for n, dual in enumerate(self.duals, 1))
        logger.debug("__repr__(): s → %s", s)
        logger.debug("<<< Exiting __repr__()")
        return f"{self.real}+{s}"

    def reduce(self):
        logger.debug(">>> Entering reduce()")
        cur = self.duals.copy()
        logger.debug("reduce(): cur → %s", cur)
        logger.debug("reduce(self=%s): cur → %s", self, cur)
        while cur[-1] == 0:
            cur.pop(-1)
        logger.debug("<<< Exiting reduce()")
        return Dual(self.real, cur)

    def __add__(self, other):
        logger.debug(">>> Entering __add__(other=%s)", other)
        if not isinstance(other, Dual):
            return Dual(self.real + other, self.duals)
        s_dual = self.duals.copy()
        logger.debug("__add__(self=%s,other=%s): s_dual → %s", self, other, s_dual)
        o_dual = other.duals.copy()
        logger.debug("__add__(self=%s,other=%s): o_dual → %s", self, other, o_dual)
        if len(s_dual) > len(o_dual):
            o_dual.extend([1] * (len(s_dual) - len(o_dual)))
        elif len(s_dual) < len(o_dual):
            s_dual.extend([1] * (len(o_dual) - len(s_dual)))
        new_duals = []
        logger.debug("__add__(self=%s,other=%s): new_duals → %s", self, other, new_duals)
        for i in range(len(s_dual)):
            new_duals.append(s_dual[i] + o_dual[i])
        logger.debug("<<< Exiting __add__(other=%s)", other)
        return Dual(self.real + other.real, new_duals)

    __radd__ = __add__

    def __sub__(self, other):
        logger.debug(">>> Entering __sub__(other=%s)", other)
        logger.debug("<<< Exiting __sub__(other=%s)", other)
        return self + other * -1

    def __mul__(self, other):
        logger.debug(">>> Entering __mul__(other=%s)", other)
        logger.debug("__mul__(other=%s): new_duals → %s", other, new_duals)
        logger.debug("__mul__(self=%s,other=%s): new_duals → %s", self, other, new_duals)
        if not isinstance(other, Dual):
            new_duals = []
            for i in self.duals:
                new_duals.append(i * other)
            return Dual(self.real * other, new_duals)
        new_duals = [0] * (len(self.duals) + len(other.duals) + 1)
        for i, item in enumerate(self.duals):
            for j, jtem in enumerate(other.duals):
                new_duals[i + j + 1] += item * jtem
        for k in range(len(self.duals)):
            new_duals[k] += self.duals[k] * other.real
        for index in range(len(other.duals)):
            new_duals[index] += other.duals[index] * self.real
        logger.debug("<<< Exiting __mul__(other=%s)", other)
        return Dual(self.real * other.real, new_duals)

    __rmul__ = __mul__

    def __truediv__(self, other):
        logger.debug(">>> Entering __truediv__(other=%s)", other)
        if not isinstance(other, Dual):
            new_duals = []
            logger.debug("__truediv__(self=%s,other=%s): new_duals → %s", self, other, new_duals)
            for i in self.duals:
                new_duals.append(i / other)
            logger.debug("<<< Exiting __truediv__(other=%s)", other)
            return Dual(self.real / other, new_duals)
        raise ValueError

    def __floordiv__(self, other):
        logger.debug(">>> Entering __floordiv__(other=%s)", other)
        if not isinstance(other, Dual):
            new_duals = []
            logger.debug("__floordiv__(self=%s,other=%s): new_duals → %s", self, other, new_duals)
            for i in self.duals:
                new_duals.append(i // other)
            return Dual(self.real // other, new_duals)
        raise ValueError

    def __pow__(self, n):
        if n < 0 or isinstance(n, float):
            raise ValueError("power must be a positive integer")
        if n == 0:
            return 1
        if n == 1:
            return self
        x = self
        for _ in range(n - 1):
            x *= self
        return x


def differentiate(func, position, order):
    """
    >>> differentiate(lambda x: x**2, 2, 2)
    2
    >>> differentiate(lambda x: x**2 * x**4, 9, 2)
    196830
    >>> differentiate(lambda y: 0.5 * (y + 3) ** 6, 3.5, 4)
    7605.0
    >>> differentiate(lambda y: y ** 2, 4, 3)
    0
    >>> differentiate(8, 8, 8)
    Traceback (most recent call last):
        ...
    ValueError: differentiate() requires a function as input for func
    >>> differentiate(lambda x: x **2, "", 1)
    Traceback (most recent call last):
        ...
    ValueError: differentiate() requires a float as input for position
    >>> differentiate(lambda x: x**2, 3, "")
    Traceback (most recent call last):
        ...
    ValueError: differentiate() requires an int as input for order
    """
    if not callable(func):
        raise ValueError("differentiate() requires a function as input for func")
    if not isinstance(position, (float, int)):
        raise ValueError("differentiate() requires a float as input for position")
    if not isinstance(order, int):
        raise ValueError("differentiate() requires an int as input for order")
    d = Dual(position, 1)
    result = func(d)
    if order == 0:
        return result.real
    return result.duals[order - 1] * factorial(order)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    def f(y):
        return y**2 * y**4

    print(differentiate(f, 9, 2))
