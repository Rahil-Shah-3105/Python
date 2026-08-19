"""

This module implements a single indeterminate polynomials class
with some basic operations

Reference: https://en.wikipedia.org/wiki/Polynomial

"""

from __future__ import annotations

from collections.abc import MutableSequence
import logging
logger = logging.getLogger(__name__)


class Polynomial:
    def __init__(self, degree: int, coefficients: MutableSequence[float]) -> None:
        """
        The coefficients should be in order of degree, from smallest to largest.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p = Polynomial(2, [1, 2, 3, 4])
        Traceback (most recent call last):
        ...
        ValueError: The number of coefficients should be equal to the degree + 1.

        """
        logger.debug(">>> Entering __init__(degree=%s,coefficients=%s)", degree, coefficients)
        if len(coefficients) != degree + 1:
            raise ValueError(
                "The number of coefficients should be equal to the degree + 1."
            )

        self.coefficients: list[float] = list(coefficients)
        logger.debug("<<< Exiting __init__(degree=%s,coefficients=%s)", degree, coefficients)
        self.degree = degree
        logger.debug("__init__(self=%s,degree=%s,coefficients=%s): self.degree → %s", self, degree, coefficients, self.degree)

    def __add__(self, polynomial_2: Polynomial) -> Polynomial:
        """
        Polynomial addition
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p + q
        6x^2 + 4x + 2
        """
        logger.debug(">>> Entering __add__(polynomial_2=%s)", polynomial_2)

        if self.degree > polynomial_2.degree:
            coefficients = self.coefficients[:]
            logger.debug("__add__(self=%s,polynomial_2=%s): coefficients → %s", self, polynomial_2, coefficients)
            for i in range(polynomial_2.degree + 1):
                coefficients[i] += polynomial_2.coefficients[i]
            return Polynomial(self.degree, coefficients)
        else:
            coefficients = polynomial_2.coefficients[:]
            for i in range(self.degree + 1):
                coefficients[i] += self.coefficients[i]
            logger.debug("<<< Exiting __add__(polynomial_2=%s)", polynomial_2)
            return Polynomial(polynomial_2.degree, coefficients)

    def __sub__(self, polynomial_2: Polynomial) -> Polynomial:
        """
        Polynomial subtraction
        >>> p = Polynomial(2, [1, 2, 4])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p - q
        1x^2
        """
        logger.debug(">>> Entering __sub__(polynomial_2=%s)", polynomial_2)
        logger.debug("<<< Exiting __sub__(polynomial_2=%s)", polynomial_2)
        return self + polynomial_2 * Polynomial(0, [-1])

    def __neg__(self) -> Polynomial:
        """
        Polynomial negation
        >>> p = Polynomial(2, [1, 2, 3])
        >>> -p
         - 3x^2 - 2x - 1
        """
        logger.debug(">>> Entering __neg__()")
        logger.debug("<<< Exiting __neg__()")
        return Polynomial(self.degree, [-c for c in self.coefficients])

    def __mul__(self, polynomial_2: Polynomial) -> Polynomial:
        """
        Polynomial multiplication
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p * q
        9x^4 + 12x^3 + 10x^2 + 4x + 1
        """
        logger.debug(">>> Entering __mul__(polynomial_2=%s)", polynomial_2)
        coefficients: list[float] = [0] * (self.degree + polynomial_2.degree + 1)
        for i in range(self.degree + 1):
            for j in range(polynomial_2.degree + 1):
                coefficients[i + j] += (
                    self.coefficients[i] * polynomial_2.coefficients[j]
                )

        logger.debug("<<< Exiting __mul__(polynomial_2=%s)", polynomial_2)
        return Polynomial(self.degree + polynomial_2.degree, coefficients)

    def evaluate(self, substitution: float) -> float:
        """
        Evaluates the polynomial at x.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p.evaluate(2)
        17
        """
        logger.debug(">>> Entering evaluate(substitution=%s)", substitution)
        result: int | float = 0
        for i in range(self.degree + 1):
            result += self.coefficients[i] * (substitution**i)
        logger.debug("<<< Exiting evaluate(substitution=%s)", substitution)
        return result

    def __str__(self) -> str:
        """
        >>> p = Polynomial(2, [1, 2, 3])
        >>> print(p)
        3x^2 + 2x + 1
        """
        logger.debug(">>> Entering __str__()")
        polynomial = ""
        logger.debug("__str__(self=%s): polynomial → %s", self, polynomial)
        logger.debug("__str__(): polynomial → %s", polynomial)
        for i in range(self.degree, -1, -1):
            if self.coefficients[i] == 0:
                continue
            elif self.coefficients[i] > 0:
                if polynomial:
                    polynomial += " + "
            else:
                polynomial += " - "

            if i == 0:
                polynomial += str(abs(self.coefficients[i]))
            elif i == 1:
                polynomial += str(abs(self.coefficients[i])) + "x"
            else:
                polynomial += str(abs(self.coefficients[i])) + "x^" + str(i)

        logger.debug("<<< Exiting __str__()")
        return polynomial

    def __repr__(self) -> str:
        """
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p
        3x^2 + 2x + 1
        """
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return self.__str__()

    def derivative(self) -> Polynomial:
        """
        Returns the derivative of the polynomial.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p.derivative()
        6x + 2
        """
        logger.debug(">>> Entering derivative()")
        coefficients: list[float] = [0] * self.degree
        for i in range(self.degree):
            coefficients[i] = self.coefficients[i + 1] * (i + 1)
        logger.debug("<<< Exiting derivative()")
        return Polynomial(self.degree - 1, coefficients)

    def integral(self, constant: float = 0) -> Polynomial:
        """
        Returns the integral of the polynomial.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> p.integral()
        1.0x^3 + 1.0x^2 + 1.0x
        """
        logger.debug(">>> Entering integral(constant=%s)", constant)
        coefficients: list[float] = [0] * (self.degree + 2)
        coefficients[0] = constant
        for i in range(self.degree + 1):
            coefficients[i + 1] = self.coefficients[i] / (i + 1)
        logger.debug("<<< Exiting integral(constant=%s)", constant)
        return Polynomial(self.degree + 1, coefficients)

    def __eq__(self, polynomial_2: object) -> bool:
        """
        Checks if two polynomials are equal.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p == q
        True
        """
        logger.debug(">>> Entering __eq__(polynomial_2=%s)", polynomial_2)
        if not isinstance(polynomial_2, Polynomial):
            return False

        if self.degree != polynomial_2.degree:
            return False

        for i in range(self.degree + 1):
            if self.coefficients[i] != polynomial_2.coefficients[i]:
                return False

        logger.debug("<<< Exiting __eq__(polynomial_2=%s)", polynomial_2)
        return True

    def __ne__(self, polynomial_2: object) -> bool:
        """
        Checks if two polynomials are not equal.
        >>> p = Polynomial(2, [1, 2, 3])
        >>> q = Polynomial(2, [1, 2, 3])
        >>> p != q
        False
        """
        logger.debug(">>> Entering __ne__(polynomial_2=%s)", polynomial_2)
        logger.debug("<<< Exiting __ne__(polynomial_2=%s)", polynomial_2)
        return not self.__eq__(polynomial_2)
