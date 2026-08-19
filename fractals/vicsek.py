"""Authors Bastien Capiaux & Mehdi Oudghiri

The Vicsek fractal algorithm is a recursive algorithm that creates a
pattern known as the Vicsek fractal or the Vicsek square.
It is based on the concept of self-similarity, where the pattern at each
level of recursion resembles the overall pattern.
The algorithm involves dividing a square into 9 equal smaller squares,
removing the center square, and then repeating this process on the remaining 8 squares.
This results in a pattern that exhibits self-similarity and has a
square-shaped outline with smaller squares within it.

Source: https://en.wikipedia.org/wiki/Vicsek_fractal
"""

import turtle
import logging
logger = logging.getLogger(__name__)


def draw_cross(x: float, y: float, length: float):
    """
    Draw a cross at the specified position and with the specified length.
    """
    logger.debug(">>> Entering draw_cross(x=%s,y=%s,length=%s)", x, y, length)
    turtle.up()
    turtle.goto(x - length / 2, y - length / 6)
    turtle.down()
    turtle.seth(0)
    logger.debug("draw_cross(x=%s,y=%s,length=%s): turtle → %s", x, y, length, turtle)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length / 3)
        turtle.right(90)
        turtle.fd(length / 3)
        turtle.left(90)
        turtle.fd(length / 3)
        turtle.left(90)
    turtle.end_fill()
    logger.debug("<<< Exiting draw_cross(x=%s,y=%s,length=%s)", x, y, length)


def draw_fractal_recursive(x: float, y: float, length: float, depth: float):
    """
    Recursively draw the Vicsek fractal at the specified position, with the
    specified length and depth.
    """
    logger.debug(">>> Entering draw_fractal_recursive(x=%s,y=%s,length=%s,depth=%s)", x, y, length, depth)
    if depth == 0:
        draw_cross(x, y, length)
        logger.debug("<<< Exiting draw_fractal_recursive(x=%s,y=%s,length=%s,depth=%s)", x, y, length, depth)
        return

    draw_fractal_recursive(x, y, length / 3, depth - 1)
    draw_fractal_recursive(x + length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x - length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x, y + length / 3, length / 3, depth - 1)
    draw_fractal_recursive(x, y - length / 3, length / 3, depth - 1)


def set_color(rgb: str):
    logger.debug(">>> Entering set_color(rgb=%s)", rgb)
    turtle.color(rgb)
    logger.debug("<<< Exiting set_color(rgb=%s)", rgb)


def draw_vicsek_fractal(x: float, y: float, length: float, depth: float, color="blue"):
    """
    Draw the Vicsek fractal at the specified position, with the specified
    length and depth.
    """
    logger.debug(">>> Entering draw_vicsek_fractal(x=%s,y=%s,length=%s,depth=%s,color=%s)", x, y, length, depth, color)
    turtle.speed(0)
    turtle.hideturtle()
    set_color(color)
    import time; __log_start = time.time()
    draw_fractal_recursive(x, y, length, depth)
    logger.debug("<<< Exiting draw_vicsek_fractal(x=%s,y=%s,length=%s,depth=%s,color=%s)", x, y, length, depth, color)
    logger.info("draw_vicsek_fractal(x,y,length,depth,color)=%s,%s,%s,%s,%s: update operation took %s ms", x, y, length, depth, color, int((time.time() - __log_start) * 1000))
    turtle.Screen().update()


def main():
    logger.debug(">>> Entering main()")
    draw_vicsek_fractal(0, 0, 800, 4)

    turtle.done()
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
