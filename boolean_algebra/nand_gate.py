"""
A NAND Gate is a logic gate in boolean algebra which results to 0 (False) if both
the inputs are 1, and 1 (True) otherwise. It's similar to adding
a NOT gate along with an AND gate.
Following is the truth table of a NAND Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    1   |
    |    0    |    1    |    1   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------
Refer - https://www.geeksforgeeks.org/logic-gates-in-python/
"""
import logging
logger = logging.getLogger(__name__)


def nand_gate(input_1: int, input_2: int) -> int:
    """
    Calculate NAND of the input values
    >>> nand_gate(0, 0)
    1
    >>> nand_gate(0, 1)
    1
    >>> nand_gate(1, 0)
    1
    >>> nand_gate(1, 1)
    0
    """
    logger.error(">>> Entering nand_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "nand_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    logger.warning("<<< Exiting nand_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "nand_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    return int(not (input_1 and input_2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
