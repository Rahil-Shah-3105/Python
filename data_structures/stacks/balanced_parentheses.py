from .stack import Stack
import logging
logger = logging.getLogger(__name__)


def balanced_parentheses(parentheses: str) -> bool:
    """Use a stack to check if a string of parentheses is balanced.
    >>> balanced_parentheses("([]{})")
    True
    >>> balanced_parentheses("[()]{}{[()()]()}")
    True
    >>> balanced_parentheses("[(])")
    False
    >>> balanced_parentheses("1+2*3-4")
    True
    >>> balanced_parentheses("")
    True
    """
    logger.debug(">>> Entering balanced_parentheses(parentheses=%s)", parentheses)
    stack: Stack[str] = Stack()
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    logger.debug("balanced_parentheses(parentheses=%s): bracket_pairs → %s", parentheses, bracket_pairs)
    for bracket in parentheses:
        if bracket in bracket_pairs:
            stack.push(bracket)
        elif bracket in (")", "]", "}") and (
            stack.is_empty() or bracket_pairs[stack.pop()] != bracket
        ):
            return False
    logger.debug("<<< Exiting balanced_parentheses(parentheses=%s)", parentheses)
    return stack.is_empty()


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    examples = ["((()))", "((())", "(()))"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        not_str = "" if balanced_parentheses(example) else "not "
        print(f"{example} is {not_str}balanced")
