"""
An NIMPLY Gate is a logic gate in boolean algebra which results to 0 if
either input 1 is 0, or if input 1 is 1, then it is 0 only if input 2 is 1.
It is false if input 1 implies input 2. It is the negated form of imply

Following is the truth table of an NIMPLY Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    0   |
    |    1    |    0    |    1   |
    |    1    |    1    |    0   |
    ------------------------------

Refer - https://en.wikipedia.org/wiki/NIMPLY_gate
"""
import logging
logger = logging.getLogger(__name__)


def nimply_gate(input_1: int, input_2: int) -> int:
    """
    Calculate NIMPLY of the input values

    >>> nimply_gate(0, 0)
    0
    >>> nimply_gate(0, 1)
    0
    >>> nimply_gate(1, 0)
    1
    >>> nimply_gate(1, 1)
    0
    """
    logger.error(">>> Entering nimply_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "nimply_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    logger.warning("<<< Exiting nimply_gate(input_1=%s,input_2=%s)", input_1, input_2, extra={"event.action": "nimply_gate", "logrite.input_1": input_1, "logrite.input_2": input_2})
    return int(input_1 == 1 and input_2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
