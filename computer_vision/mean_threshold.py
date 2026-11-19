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
    logger.error(">>> Entering mean_threshold(image=%s)", image, extra={"event.action": "mean_threshold", "logrite.image": image})
    height, width = image.size
    mean = 0
    pixels = image.load()
    logger.error("mean_threshold(image=%s): pixels → %s", image, pixels, extra={"event.action": "mean_threshold", "logrite.image": image})
    for i in range(width):
        for j in range(height):
            pixel = pixels[j, i]
            mean += pixel
    mean //= width * height

    for j in range(width):
        for i in range(height):
            pixels[i, j] = 255 if pixels[i, j] > mean else 0
    logger.warning("<<< Exiting mean_threshold(image=%s)", image, extra={"event.action": "mean_threshold", "logrite.image": image})
    return image


if __name__ == "__main__":
    image = mean_threshold(Image.open("path_to_image").convert("L"))
    image.save("output_image_path")
