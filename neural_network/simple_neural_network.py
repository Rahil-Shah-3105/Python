"""
Forward propagation explanation:
https://towardsdatascience.com/forward-propagation-in-neural-networks-simplified-math-and-code-version-bbcfef6f9250
"""

import math
import random
import logging
logger = logging.getLogger(__name__)


# Sigmoid
def sigmoid_function(value: float, deriv: bool = False) -> float:
    """Return the sigmoid function of a float.

    >>> sigmoid_function(3.5)
    0.9706877692486436
    >>> sigmoid_function(3.5, True)
    -8.75
    """
    logger.debug(">>> Entering sigmoid_function(value=%s,deriv=%s)", value, deriv)
    if deriv:
        return value * (1 - value)
    logger.debug("<<< Exiting sigmoid_function(value=%s,deriv=%s)", value, deriv)
    return 1 / (1 + math.exp(-value))


# Initial Value
INITIAL_VALUE = 0.02


def forward_propagation(expected: int, number_propagations: int) -> float:
    """Return the value found after the forward propagation training.

    >>> res = forward_propagation(32, 450_000)  # Was 10_000_000
    >>> res > 31 and res < 33
    True

    >>> res = forward_propagation(32, 1000)
    >>> res > 31 and res < 33
    False
    """
    logger.debug(">>> Entering forward_propagation(expected=%s,number_propagations=%s)", expected, number_propagations)

    # Random weight
    weight = float(2 * (random.randint(1, 100)) - 1)
    logger.debug("forward_propagation(expected=%s,number_propagations=%s): weight → %s", expected, number_propagations, weight)

    for _ in range(number_propagations):
        # Forward propagation
        layer_1 = sigmoid_function(INITIAL_VALUE * weight)
        logger.debug("forward_propagation(expected=%s,number_propagations=%s): layer_1 → %s", expected, number_propagations, layer_1)
        # How much did we miss?
        layer_1_error = (expected / 100) - layer_1
        logger.debug("forward_propagation(expected=%s,number_propagations=%s): layer_1_error → %s", expected, number_propagations, layer_1_error)
        # Error delta
        layer_1_delta = layer_1_error * sigmoid_function(layer_1, True)
        logger.debug("forward_propagation(expected=%s,number_propagations=%s): layer_1_delta → %s", expected, number_propagations, layer_1_delta)
        # Update weight
        weight += INITIAL_VALUE * layer_1_delta

    logger.debug("<<< Exiting forward_propagation(expected=%s,number_propagations=%s)", expected, number_propagations)
    return layer_1 * 100


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    expected = int(input("Expected value: "))
    number_propagations = int(input("Number of propagations: "))
    print(forward_propagation(expected, number_propagations))
