import logging
logger = logging.getLogger(__name__)
def largest_rectangle_area(heights: list[int]) -> int:
    """
    Inputs an array of integers representing the heights of bars,
    and returns the area of the largest rectangle that can be formed

    >>> largest_rectangle_area([2, 1, 5, 6, 2, 3])
    10

    >>> largest_rectangle_area([2, 4])
    4

    >>> largest_rectangle_area([6, 2, 5, 4, 5, 1, 6])
    12

    >>> largest_rectangle_area([1])
    1
    """
    logger.debug(">>> Entering largest_rectangle_area(heights=%s)", heights)
    stack: list[int] = []
    max_area = 0
    logger.debug("largest_rectangle_area(heights=%s): max_area → %s", heights, max_area)
    heights = [*heights, 0]  # make a new list by appending the sentinel 0
    n = len(heights)
    logger.debug("largest_rectangle_area(heights=%s): n → %s", heights, n)

    for i in range(n):
        # make sure the stack remains in increasing order
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]  # height of the bar
            logger.debug("largest_rectangle_area(heights=%s): h → %s", heights, h)
            # if stack is empty, it means entire width can be taken from index 0 to i-1
            w = i if not stack else i - stack[-1] - 1  # calculate width
            max_area = max(max_area, h * w)

        stack.append(i)

    logger.debug("<<< Exiting largest_rectangle_area(heights=%s)", heights)
    return max_area


if __name__ == "__main__":
    import doctest

    doctest.testmod()
