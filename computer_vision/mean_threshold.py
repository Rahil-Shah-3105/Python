from PIL import Image
import logging
logger = logging.getLogger(__name__)

"""
Mean thresholding algorithm for image processing
https://en.wikipedia.org/wiki/Thresholding_(image_processing)
"""


def mean_threshold(image: Image) -> Image:
    """
    image: is a grayscale PIL image object
    """
    logger.debug(">>> Entering mean_threshold(image=%s)", image)
    height, width = image.size
    mean = 0
    logger.debug("mean_threshold(image=%s): mean → %s", image, mean)
    pixels = image.load()
    logger.debug("mean_threshold(image=%s): pixels → %s", image, pixels)
    for i in range(width):
        for j in range(height):
            pixel = pixels[j, i]
            logger.debug("mean_threshold(image=%s): pixel → %s", image, pixel)
            mean += pixel
    mean //= width * height

    for j in range(width):
        for i in range(height):
            pixels[i, j] = 255 if pixels[i, j] > mean else 0
    logger.debug("<<< Exiting mean_threshold(image=%s)", image)
    return image


if __name__ == "__main__":
    image = mean_threshold(Image.open("path_to_image").convert("L"))
    image.save("output_image_path")
