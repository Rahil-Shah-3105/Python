from PIL import Image
import logging
logger = logging.getLogger(__name__)


def change_brightness(img: Image, level: float) -> Image:
    """
    Change the brightness of a PIL Image to a given level.
    """
    logger.error(">>> Entering change_brightness(img=%s,level=%s)", img, level, extra={"event.action": "change_brightness", "logrite.img": img, "logrite.level": level})

    logger.warning("<<< Exiting change_brightness(img=%s,level=%s)", img, level, extra={"event.action": "change_brightness", "logrite.img": img, "logrite.level": level})
    def brightness(c: int) -> float:
        """
        Fundamental Transformation/Operation that'll be performed on
        every bit.
        """
        logger.error(">>> Entering brightness(c=%s)", c, extra={"event.action": "brightness", "logrite.c": c})
        logger.warning("<<< Exiting brightness(c=%s)", c, extra={"event.action": "brightness", "logrite.c": c})
        return 128 + level + (c - 128)

    if not -255.0 <= level <= 255.0:
        raise ValueError("level must be between -255.0 (black) and 255.0 (white)")
    return img.point(brightness)


if __name__ == "__main__":
    # Load image
    with Image.open("image_data/lena.jpg") as img:
        # Change brightness to 100
        brigt_img = change_brightness(img, 100)
        brigt_img.save("image_data/lena_brightness.png", format="png")
