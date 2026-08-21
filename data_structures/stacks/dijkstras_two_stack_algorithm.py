"""
Author: Alexander Joslin
GitHub: github.com/echoaj

Explanation:  https://medium.com/@haleesammar/implemented-in-js-dijkstras-2-stack-
              algorithm-for-evaluating-mathematical-expressions-fc0837dae1ea

We can use Dijkstra's two stack algorithm to solve an equation
such as: (5 + ((4 * 2) * (2 + 3)))

THESE ARE THE ALGORITHM'S RULES:
RULE 1: Scan the expression from left to right. When an operand is encountered,
        push it onto the operand stack.

RULE 2: When an operator is encountered in the expression,
        push it onto the operator stack.

RULE 3: When a left parenthesis is encountered in the expression, ignore it.

RULE 4: When a right parenthesis is encountered in the expression,
        pop an operator off the operator stack.  The two operands it must
        operate on must be the last two operands pushed onto the operand stack.
        We therefore pop the operand stack twice, perform the operation,
        and push the result back onto the operand stack so it will be available
        for use as an operand of the next operator popped off the operator stack.

RULE 5: When the entire infix expression has been scanned, the value left on
        the operand stack represents the value of the expression.

NOTE:   It only works with whole numbers.
"""

__author__ = "Alexander Joslin"

import operator as op

from .stack import Stack
import logging
logger = logging.getLogger(__name__)


def dijkstras_two_stack_algorithm(equation: str) -> int:
    """
    DocTests
    >>> dijkstras_two_stack_algorithm("(5 + 3)")
    8
    >>> dijkstras_two_stack_algorithm("((9 - (2 + 9)) + (8 - 1))")
    5
    >>> dijkstras_two_stack_algorithm("((((3 - 2) - (2 + 3)) + (2 - 4)) + 3)")
    -3

    :param equation: a string
    :return: result: an integer
    """
    logger.debug(">>> Entering dijkstras_two_stack_algorithm(equation=%s)", equation)
    operators = {"*": op.mul, "/": op.truediv, "+": op.add, "-": op.sub}
    logger.debug("dijkstras_two_stack_algorithm(equation=%s): operators → %s", equation, operators)

    operand_stack: Stack[int] = Stack()
    operator_stack: Stack[str] = Stack()

    for i in equation:
        if i.isdigit():
            # RULE 1
            operand_stack.push(int(i))
        elif i in operators:
            # RULE 2
            operator_stack.push(i)
        elif i == ")":
            # RULE 4
            opr = operator_stack.peek()
            logger.debug("dijkstras_two_stack_algorithm(equation=%s): opr → %s", equation, opr)
            operator_stack.pop()
            num1 = operand_stack.peek()
            logger.debug("dijkstras_two_stack_algorithm(equation=%s): num1 → %s", equation, num1)
            operand_stack.pop()
            num2 = operand_stack.peek()
            logger.debug("dijkstras_two_stack_algorithm(equation=%s): num2 → %s", equation, num2)
            operand_stack.pop()

            total = operators[opr](num2, num1)
            logger.debug("dijkstras_two_stack_algorithm(equation=%s): total → %s", equation, total)
            operand_stack.push(total)

    # RULE 5
    logger.debug("<<< Exiting dijkstras_two_stack_algorithm(equation=%s)", equation)
    return operand_stack.peek()


if __name__ == "__main__":
    equation = "(5 + ((4 * 2) * (2 + 3)))"
    # answer = 45
    print(f"{equation} = {dijkstras_two_stack_algorithm(equation)}")
