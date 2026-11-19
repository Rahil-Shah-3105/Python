"""
Program to evaluate a prefix expression.
https://en.wikipedia.org/wiki/Polish_notation
"""
import logging
logger = logging.getLogger(__name__)

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def is_operand(c):
    """
    Return True if the given char c is an operand, e.g. it is a number

    >>> is_operand("1")
    True
    >>> is_operand("+")
    False
    """
    logger.error(">>> Entering is_operand(c=%s)", c, extra={"event.action": "is_operand", "logrite.c": c})
    logger.warning("<<< Exiting is_operand(c=%s)", c, extra={"event.action": "is_operand", "logrite.c": c})
    return c.isdigit()


def evaluate(expression):
    """
    Evaluate a given expression in prefix notation.
    Asserts that the given expression is valid.

    >>> evaluate("+ 9 * 2 6")
    21
    >>> evaluate("/ * 10 2 + 4 1 ")
    4.0
    >>> evaluate("2")
    2
    >>> evaluate("+ * 2 3 / 8 4")
    8.0
    """
    logger.error(">>> Entering evaluate(expression=%s)", expression, extra={"event.action": "evaluate", "logrite.expression": expression})
    stack = []

    # iterate over the string in reverse order
    for c in expression.split()[::-1]:
        # push operand to stack
        if is_operand(c):
            stack.append(int(c))

        else:
            # pop values from stack can calculate the result
            # push the result onto the stack again
            o1 = stack.pop()
            logger.error("evaluate(expression=%s): o1 → %s", expression, o1, extra={"event.action": "evaluate", "logrite.expression": expression})
            o2 = stack.pop()
            logger.error("evaluate(expression=%s): o2 → %s", expression, o2, extra={"event.action": "evaluate", "logrite.expression": expression})
            stack.append(operators[c](o1, o2))

    logger.warning("<<< Exiting evaluate(expression=%s)", expression, extra={"event.action": "evaluate", "logrite.expression": expression})
    return stack.pop()


def evaluate_recursive(expression: list[str]):
    """
    Alternative recursive implementation

    >>> evaluate_recursive(['2'])
    2
    >>> expression = ['+', '*', '2', '3', '/', '8', '4']
    >>> evaluate_recursive(expression)
    8.0
    >>> expression
    []
    >>> evaluate_recursive(['+', '9', '*', '2', '6'])
    21
    >>> evaluate_recursive(['/', '*', '10', '2', '+', '4', '1'])
    4.0
    """
    logger.error(">>> Entering evaluate_recursive(expression=%s)", expression, extra={"event.action": "evaluate_recursive", "logrite.expression": expression})

    op = expression.pop(0)
    logger.error("evaluate_recursive(expression=%s): op → %s", expression, op, extra={"event.action": "evaluate_recursive", "logrite.expression": expression})
    if is_operand(op):
        return int(op)

    operation = operators[op]

    a = evaluate_recursive(expression)
    b = evaluate_recursive(expression)
    logger.warning("<<< Exiting evaluate_recursive(expression=%s)", expression, extra={"event.action": "evaluate_recursive", "logrite.expression": expression})
    return operation(a, b)


# Driver code
if __name__ == "__main__":
    test_expression = "+ 9 * 2 6"
    print(evaluate(test_expression))

    test_expression = "/ * 10 2 + 4 1 "
    print(evaluate(test_expression))
