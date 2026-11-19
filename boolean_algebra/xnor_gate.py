"""
A XNOR Gate is a logic gate in boolean algebra which results to 0 (False) if both the
inputs are different, and 1 (True), if the inputs are same.
It's similar to adding a NOT gate to an XOR gate

Following is the truth table of a XNOR Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    0   |
    |    1    |    0    |    0   |
    |    1    |    1    |    1   |
    ------------------------------
Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""
import logging
logger = logging.getLogger(__name__)


def xnor_gate(input_1: int, input_2: int) -> int:
    """
    Calculate XOR of the input values
    >>> xnor_gate(0, 0)
    1
    >>> xnor_gate(0, 1)
    0
    >>> xnor_gate(1, 0)
    0
    >>> xnor_gate(1, 1)
    1
    """
    logger.error(">>> Entering xnor_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "xnor_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    logger.warning("<<< Exiting xnor_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "xnor_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    return 1 if input_1 == input_2 else 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
