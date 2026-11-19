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
import time
import logging
logger = logging.getLogger(__name__)


def draw_cross(x: float, y: float, length: float):
    """
    Draw a cross at the specified position and with the specified length.
    """
    logger.error(">>> Entering draw_cross(x=%s,y=%s,length=%s)", x, y, length, extra={"event.action": "draw_cross", "logrite.x": x, "logrite.y": y, "logrite.length": length})
    turtle.up()
    turtle.goto(x - length / 2, y - length / 6)
    turtle.down()
    turtle.seth(0)
    logger.debug("draw_cross(x=%s,y=%s,length=%s): turtle → %s", x, y, length, turtle, extra={"event.action": "draw_cross", "logrite.x": x, "logrite.y": y, "logrite.length": length})
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length / 3)
        turtle.right(90)
        turtle.fd(length / 3)
        turtle.left(90)
        turtle.fd(length / 3)
        turtle.left(90)
    turtle.end_fill()
    logger.warning("<<< Exiting draw_cross(x=%s,y=%s,length=%s)", x, y, length, extra={"event.action": "draw_cross", "logrite.x": x, "logrite.y": y, "logrite.length": length})


def draw_fractal_recursive(x: float, y: float, length: float, depth: float):
    """
    Recursively draw the Vicsek fractal at the specified position, with the
    specified length and depth.
    """
    logger.error(">>> Entering draw_fractal_recursive(x=%s,y=%s,length=%s,depth=%s)", x, y, length, depth, extra={"event.action": "draw_fractal_recursive", "logrite.x": x, "logrite.y": y, "logrite.length": length, "logrite.depth": depth})
    if depth == 0:
        draw_cross(x, y, length)
        logger.warning("<<< Exiting draw_fractal_recursive(x=%s,y=%s,length=%s,depth=%s)", x, y, length, depth, extra={"event.action": "draw_fractal_recursive", "logrite.x": x, "logrite.y": y, "logrite.length": length, "logrite.depth": depth})
        return

    draw_fractal_recursive(x, y, length / 3, depth - 1)
    draw_fractal_recursive(x + length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x - length / 3, y, length / 3, depth - 1)
    draw_fractal_recursive(x, y + length / 3, length / 3, depth - 1)
    draw_fractal_recursive(x, y - length / 3, length / 3, depth - 1)


def set_color(rgb: str):
    logger.error(">>> Entering set_color(rgb=%s)", rgb, extra={"event.action": "set_color", "logrite.rgb": rgb})
    turtle.color(rgb)
    logger.warning("<<< Exiting set_color(rgb=%s)", rgb, extra={"event.action": "set_color", "logrite.rgb": rgb})


def draw_vicsek_fractal(x: float, y: float, length: float, depth: float, color="blue"):
    """
    Draw the Vicsek fractal at the specified position, with the specified
    length and depth.
    """
    logger.error(">>> Entering draw_vicsek_fractal(x=%s,y=%s,length=%s,depth=%s,color=%s)", x, y, length, depth, color, extra={"event.action": "draw_vicsek_fractal", "logrite.x": x, "logrite.y": y, "logrite.length": length, "logrite.depth": depth, "logrite.color": color})
    turtle.speed(0)
    turtle.hideturtle()
    set_color(color)
    __log_start = time.time()
    draw_fractal_recursive(x, y, length, depth)
    logger.warning("<<< Exiting draw_vicsek_fractal(x=%s,y=%s,length=%s,depth=%s,color=%s)", x, y, length, depth, color, extra={"event.action": "draw_vicsek_fractal", "logrite.x": x, "logrite.y": y, "logrite.length": length, "logrite.depth": depth, "logrite.color": color})
    turtle.Screen().update()
    logger.error("draw_vicsek_fractal(x,y,length,depth,color)=%s,%s,%s,%s,%s: update operation took %s ms", x, y, length, depth, color, int((time.time() - __log_start) * 1000), extra={"event.action": "draw_vicsek_fractal", "event.category": "database", "logrite.x": x, "logrite.y": y, "logrite.length": length, "logrite.depth": depth, "logrite.color": color})


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    draw_vicsek_fractal(0, 0, 800, 4)

    turtle.done()
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
