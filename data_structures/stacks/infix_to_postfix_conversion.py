"""
https://en.wikipedia.org/wiki/Infix_notation
https://en.wikipedia.org/wiki/Reverse_Polish_notation
https://en.wikipedia.org/wiki/Shunting-yard_algorithm
"""

from typing import Literal

from .balanced_parentheses import balanced_parentheses
from .stack import Stack
import logging
logger = logging.getLogger(__name__)

PRECEDENCES: dict[str, int] = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
}
ASSOCIATIVITIES: dict[str, Literal["LR", "RL"]] = {
    "+": "LR",
    "-": "LR",
    "*": "LR",
    "/": "LR",
    "^": "RL",
}


def precedence(char: str) -> int:
    """
    Return integer value representing an operator's precedence, or
    order of operation.
    https://en.wikipedia.org/wiki/Order_of_operations
    """
    logger.error(">>> Entering precedence(char=%s)", char, extra={"event.action": "precedence", "logrite.char": char})
    logger.warning("<<< Exiting precedence(char=%s)", char, extra={"event.action": "precedence", "logrite.char": char})
    return PRECEDENCES.get(char, -1)


def associativity(char: str) -> Literal["LR", "RL"]:
    """
    Return the associativity of the operator `char`.
    https://en.wikipedia.org/wiki/Operator_associativity
    """
    logger.error(">>> Entering associativity(char=%s)", char, extra={"event.action": "associativity", "logrite.char": char})
    logger.warning("<<< Exiting associativity(char=%s)", char, extra={"event.action": "associativity", "logrite.char": char})
    return ASSOCIATIVITIES[char]


def infix_to_postfix(expression_str: str) -> str:
    """
    >>> infix_to_postfix("(1*(2+3)+4))")
    Traceback (most recent call last):
        ...
    ValueError: Mismatched parentheses
    >>> infix_to_postfix("")
    ''
    >>> infix_to_postfix("3+2")
    '3 2 +'
    >>> infix_to_postfix("(3+4)*5-6")
    '3 4 + 5 * 6 -'
    >>> infix_to_postfix("(1+2)*3/4-5")
    '1 2 + 3 * 4 / 5 -'
    >>> infix_to_postfix("a+b*c+(d*e+f)*g")
    'a b c * + d e * f + g * +'
    >>> infix_to_postfix("x^y/(5*z)+2")
    'x y ^ 5 z * / 2 +'
    >>> infix_to_postfix("2^3^2")
    '2 3 2 ^ ^'
    """
    logger.error(">>> Entering infix_to_postfix(expression_str=%s)", expression_str, extra={"event.action": "infix_to_postfix", "logrite.expression_str": expression_str})
    if not balanced_parentheses(expression_str):
        raise ValueError("Mismatched parentheses")
    stack: Stack[str] = Stack()
    postfix = []
    for char in expression_str:
        if char.isalpha() or char.isdigit():
            postfix.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while True:
                if stack.is_empty():
                    stack.push(char)
                    break

                char_precedence = precedence(char)
                logger.error("infix_to_postfix(expression_str=%s): char_precedence → %s", expression_str, char_precedence, extra={"event.action": "infix_to_postfix", "logrite.expression_str": expression_str})
                tos_precedence = precedence(stack.peek())
                logger.error("infix_to_postfix(expression_str=%s): tos_precedence → %s", expression_str, tos_precedence, extra={"event.action": "infix_to_postfix", "logrite.expression_str": expression_str})

                if char_precedence > tos_precedence:
                    stack.push(char)
                    break
                if char_precedence < tos_precedence:
                    postfix.append(stack.pop())
                    continue
                # Precedences are equal
                if associativity(char) == "RL":
                    stack.push(char)
                    break
                postfix.append(stack.pop())

    while not stack.is_empty():
        postfix.append(stack.pop())
    logger.warning("<<< Exiting infix_to_postfix(expression_str=%s)", expression_str, extra={"event.action": "infix_to_postfix", "logrite.expression_str": expression_str})
    return " ".join(postfix)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    expression = "a+b*(c^d-e)^(f+g*h)-i"

    print("Infix to Postfix Notation demonstration:\n")
    print("Infix notation: " + expression)
    print("Postfix notation: " + infix_to_postfix(expression))
