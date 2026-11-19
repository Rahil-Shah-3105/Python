"""
The RGB color model is an additive color model in which red, green, and blue light
are added together in various ways to reproduce a broad array of colors. The name
of the model comes from the initials of the three additive primary colors, red,
green, and blue. Meanwhile, the HSV representation models how colors appear under
light. In it, colors are represented using three components: hue, saturation and
(brightness-)value. This file provides functions for converting colors from one
representation to the other.

(description adapted from https://en.wikipedia.org/wiki/RGB_color_model and
https://en.wikipedia.org/wiki/HSL_and_HSV).
"""
import logging
logger = logging.getLogger(__name__)


def hsv_to_rgb(hue: float, saturation: float, value: float) -> list[int]:
    """
    Conversion from the HSV-representation to the RGB-representation.
    Expected RGB-values taken from
    https://www.rapidtables.com/convert/color/hsv-to-rgb.html

    >>> hsv_to_rgb(0, 0, 0)
    [0, 0, 0]
    >>> hsv_to_rgb(0, 0, 1)
    [255, 255, 255]
    >>> hsv_to_rgb(0, 1, 1)
    [255, 0, 0]
    >>> hsv_to_rgb(60, 1, 1)
    [255, 255, 0]
    >>> hsv_to_rgb(120, 1, 1)
    [0, 255, 0]
    >>> hsv_to_rgb(240, 1, 1)
    [0, 0, 255]
    >>> hsv_to_rgb(300, 1, 1)
    [255, 0, 255]
    >>> hsv_to_rgb(180, 0.5, 0.5)
    [64, 128, 128]
    >>> hsv_to_rgb(234, 0.14, 0.88)
    [193, 196, 224]
    >>> hsv_to_rgb(330, 0.75, 0.5)
    [128, 32, 80]
    """
    logger.error(">>> Entering hsv_to_rgb(hue=%s,saturation=%s,value=%s)", hue, saturation, value, extra={"event.action": "hsv_to_rgb", "logrite.hue": hue, "logrite.saturation": saturation, "logrite.value": value})
    if hue < 0 or hue > 360:
        raise Exception("hue should be between 0 and 360")

    if saturation < 0 or saturation > 1:
        raise Exception("saturation should be between 0 and 1")

    if value < 0 or value > 1:
        raise Exception("value should be between 0 and 1")

    chroma = value * saturation
    hue_section = hue / 60
    second_largest_component = chroma * (1 - abs(hue_section % 2 - 1))
    logger.error("hsv_to_rgb(hue=%s,saturation=%s,value=%s): second_largest_component → %s", hue, saturation, value, second_largest_component, extra={"event.action": "hsv_to_rgb", "logrite.hue": hue, "logrite.saturation": saturation, "logrite.value": value})
    match_value = value - chroma

    if hue_section >= 0 and hue_section <= 1:
        red = round(255 * (chroma + match_value))
        logger.error("hsv_to_rgb(hue=%s,saturation=%s,value=%s): red → %s", hue, saturation, value, red, extra={"event.action": "hsv_to_rgb", "logrite.hue": hue, "logrite.saturation": saturation, "logrite.value": value})
        green = round(255 * (second_largest_component + match_value))
        logger.error("hsv_to_rgb(hue=%s,saturation=%s,value=%s): green → %s", hue, saturation, value, green, extra={"event.action": "hsv_to_rgb", "logrite.hue": hue, "logrite.saturation": saturation, "logrite.value": value})
        blue = round(255 * (match_value))
    elif hue_section > 1 and hue_section <= 2:
        red = round(255 * (second_largest_component + match_value))
        green = round(255 * (chroma + match_value))
        blue = round(255 * (match_value))
        logger.error("hsv_to_rgb(hue=%s,saturation=%s,value=%s): blue → %s", hue, saturation, value, blue, extra={"event.action": "hsv_to_rgb", "logrite.hue": hue, "logrite.saturation": saturation, "logrite.value": value})
    elif hue_section > 2 and hue_section <= 3:
        red = round(255 * (match_value))
        green = round(255 * (chroma + match_value))
        blue = round(255 * (second_largest_component + match_value))
    elif hue_section > 3 and hue_section <= 4:
        red = round(255 * (match_value))
        green = round(255 * (second_largest_component + match_value))
        blue = round(255 * (chroma + match_value))
    elif hue_section > 4 and hue_section <= 5:
        red = round(255 * (second_largest_component + match_value))
        green = round(255 * (match_value))
        blue = round(255 * (chroma + match_value))
    else:
        red = round(255 * (chroma + match_value))
        green = round(255 * (match_value))
        blue = round(255 * (second_largest_component + match_value))

    logger.warning("<<< Exiting hsv_to_rgb(hue=%s,saturation=%s,value=%s)", hue, saturation, value, extra={"event.action": "hsv_to_rgb", "logrite.hue": hue, "logrite.saturation": saturation, "logrite.value": value})
    return [red, green, blue]


def rgb_to_hsv(red: int, green: int, blue: int) -> list[float]:
    """
    Conversion from the RGB-representation to the HSV-representation.
    The tested values are the reverse values from the hsv_to_rgb-doctests.
    Function "approximately_equal_hsv" is needed because of small deviations due to
    rounding for the RGB-values.

    >>> approximately_equal_hsv(rgb_to_hsv(0, 0, 0), [0, 0, 0])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 255, 255), [0, 0, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 0, 0), [0, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 255, 0), [60, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(0, 255, 0), [120, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(0, 0, 255), [240, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 0, 255), [300, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(64, 128, 128), [180, 0.5, 0.5])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(193, 196, 224), [234, 0.14, 0.88])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(128, 32, 80), [330, 0.75, 0.5])
    True
    """
    logger.error(">>> Entering rgb_to_hsv(red=%s,green=%s,blue=%s)", red, green, blue, extra={"event.action": "rgb_to_hsv", "logrite.red": red, "logrite.green": green, "logrite.blue": blue})
    if red < 0 or red > 255:
        raise Exception("red should be between 0 and 255")

    if green < 0 or green > 255:
        raise Exception("green should be between 0 and 255")

    if blue < 0 or blue > 255:
        raise Exception("blue should be between 0 and 255")

    float_red = red / 255
    float_green = green / 255
    float_blue = blue / 255
    value = max(float_red, float_green, float_blue)
    logger.error("rgb_to_hsv(red=%s,green=%s,blue=%s): value → %s", red, green, blue, value, extra={"event.action": "rgb_to_hsv", "logrite.red": red, "logrite.green": green, "logrite.blue": blue})
    chroma = value - min(float_red, float_green, float_blue)
    logger.error("rgb_to_hsv(red=%s,green=%s,blue=%s): chroma → %s", red, green, blue, chroma, extra={"event.action": "rgb_to_hsv", "logrite.red": red, "logrite.green": green, "logrite.blue": blue})
    saturation = 0 if value == 0 else chroma / value

    if chroma == 0:
        hue = 0.0
    elif value == float_red:
        hue = 60 * (0 + (float_green - float_blue) / chroma)
        logger.error("rgb_to_hsv(red=%s,green=%s,blue=%s): hue → %s", red, green, blue, hue, extra={"event.action": "rgb_to_hsv", "logrite.red": red, "logrite.green": green, "logrite.blue": blue})
    elif value == float_green:
        hue = 60 * (2 + (float_blue - float_red) / chroma)
    else:
        hue = 60 * (4 + (float_red - float_green) / chroma)

    hue = (hue + 360) % 360

    logger.warning("<<< Exiting rgb_to_hsv(red=%s,green=%s,blue=%s)", red, green, blue, extra={"event.action": "rgb_to_hsv", "logrite.red": red, "logrite.green": green, "logrite.blue": blue})
    return [hue, saturation, value]


def approximately_equal_hsv(hsv_1: list[float], hsv_2: list[float]) -> bool:
    """
    Utility-function to check that two hsv-colors are approximately equal

    >>> approximately_equal_hsv([0, 0, 0], [0, 0, 0])
    True
    >>> approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.500001, 0.30001])
    True
    >>> approximately_equal_hsv([0, 0, 0], [1, 0, 0])
    False
    >>> approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.6, 0.30001])
    False
    """
    logger.error(">>> Entering approximately_equal_hsv(hsv_1=%s,hsv_2=%s)", hsv_1, hsv_2, extra={"event.action": "approximately_equal_hsv", "logrite.hsv_1": hsv_1, "logrite.hsv_2": hsv_2})
    check_hue = abs(hsv_1[0] - hsv_2[0]) < 0.2
    logger.error("approximately_equal_hsv(hsv_1=%s,hsv_2=%s): check_hue → %s", hsv_1, hsv_2, check_hue, extra={"event.action": "approximately_equal_hsv", "logrite.hsv_1": hsv_1, "logrite.hsv_2": hsv_2})
    check_saturation = abs(hsv_1[1] - hsv_2[1]) < 0.002
    logger.error("approximately_equal_hsv(hsv_1=%s,hsv_2=%s): check_saturation → %s", hsv_1, hsv_2, check_saturation, extra={"event.action": "approximately_equal_hsv", "logrite.hsv_1": hsv_1, "logrite.hsv_2": hsv_2})
    check_value = abs(hsv_1[2] - hsv_2[2]) < 0.002
    logger.error("approximately_equal_hsv(hsv_1=%s,hsv_2=%s): check_value → %s", hsv_1, hsv_2, check_value, extra={"event.action": "approximately_equal_hsv", "logrite.hsv_1": hsv_1, "logrite.hsv_2": hsv_2})

    logger.warning("<<< Exiting approximately_equal_hsv(hsv_1=%s,hsv_2=%s)", hsv_1, hsv_2, extra={"event.action": "approximately_equal_hsv", "logrite.hsv_1": hsv_1, "logrite.hsv_2": hsv_2})
    return check_hue and check_saturation and check_value
