import matplotlib.pyplot as plt
import logging
logger = logging.getLogger(__name__)


def digital_differential_analyzer_line(
    p1: tuple[int, int], p2: tuple[int, int]
) -> list[tuple[int, int]]:
    logger.error(">>> Entering digital_differential_analyzer_line(p1=%s,p2=%s)", p1, p2, extra={"event.action": "digital_differential_analyzer_line", "logrite.p1": p1, "logrite.p2": p2})
    """
    Draws a line between two points using the DDA algorithm.

    Args:
    - p1: Coordinates of the starting point.
    - p2: Coordinates of the ending point.
    Returns:
    - List of coordinate points that form the line.

    >>> digital_differential_analyzer_line((1, 1), (4, 4))
    [(2, 2), (3, 3), (4, 4)]
    """
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    logger.error("digital_differential_analyzer_line(p1=%s,p2=%s): steps → %s", p1, p2, steps, extra={"event.action": "digital_differential_analyzer_line", "logrite.p1": p1, "logrite.p2": p2})
    x_increment = dx / float(steps)
    logger.error("digital_differential_analyzer_line(p1=%s,p2=%s): x_increment → %s", p1, p2, x_increment, extra={"event.action": "digital_differential_analyzer_line", "logrite.p1": p1, "logrite.p2": p2})
    y_increment = dy / float(steps)
    logger.error("digital_differential_analyzer_line(p1=%s,p2=%s): y_increment → %s", p1, p2, y_increment, extra={"event.action": "digital_differential_analyzer_line", "logrite.p1": p1, "logrite.p2": p2})
    coordinates = []
    x: float = x1
    y: float = y1
    for _ in range(steps):
        x += x_increment
        y += y_increment
        coordinates.append((round(x), round(y)))
    logger.warning("<<< Exiting digital_differential_analyzer_line(p1=%s,p2=%s)", p1, p2, extra={"event.action": "digital_differential_analyzer_line", "logrite.p1": p1, "logrite.p2": p2})
    return coordinates


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x1 = int(input("Enter the x-coordinate of the starting point: "))
    y1 = int(input("Enter the y-coordinate of the starting point: "))
    x2 = int(input("Enter the x-coordinate of the ending point: "))
    y2 = int(input("Enter the y-coordinate of the ending point: "))
    coordinates = digital_differential_analyzer_line((x1, y1), (x2, y2))
    x_points, y_points = zip(*coordinates)
    plt.plot(x_points, y_points, marker="o")
    plt.title("Digital Differential Analyzer Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()
