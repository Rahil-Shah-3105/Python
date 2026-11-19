"""
A XOR Gate is a logic gate in boolean algebra which results to 1 (True) if only one of
the two inputs is 1, and 0 (False) if an even number of inputs are 1.
Following is the truth table of a XOR Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------

Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""
import logging
logger = logging.getLogger(__name__)


def xor_gate(input_1: int, input_2: int) -> int:
    """
    calculate xor of the input values

    >>> xor_gate(0, 0)
    0
    >>> xor_gate(0, 1)
    1
    >>> xor_gate(1, 0)
    1
    >>> xor_gate(1, 1)
    0
    """
    logger.error(">>> Entering xor_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "xor_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    logger.warning("<<< Exiting xor_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "xor_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    return (input_1, input_2).count(0) % 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
