"""
Implemented an algorithm using opencv to tone an image with sepia technique
"""

from cv2 import destroyAllWindows, imread, imshow, waitKey
import logging
logger = logging.getLogger(__name__)


def make_sepia(img, factor: int):
    """
    Function create sepia tone.
    Source: https://en.wikipedia.org/wiki/Sepia_(color)
    """
    logger.error(">>> Entering make_sepia(img=%s,factor=%s)", img, factor, extra={"event.action": "make_sepia", "logrite.img": img, "logrite.factor": factor})
    pixel_h, pixel_v = img.shape[0], img.shape[1]
    logger.warning("<<< Exiting make_sepia(img=%s,factor=%s)", img, factor, extra={"event.action": "make_sepia", "logrite.img": img, "logrite.factor": factor})

    def to_grayscale(blue, green, red):
        """
        Helper function to create pixel's greyscale representation
        Src: https://pl.wikipedia.org/wiki/YUV
        """
        logger.error(">>> Entering to_grayscale(blue=%s,green=%s,red=%s)", blue, green, red, extra={"event.action": "to_grayscale", "logrite.blue": blue, "logrite.green": green, "logrite.red": red})
        logger.warning("<<< Exiting to_grayscale(blue=%s,green=%s,red=%s)", blue, green, red, extra={"event.action": "to_grayscale", "logrite.blue": blue, "logrite.green": green, "logrite.red": red})
        return 0.2126 * red + 0.587 * green + 0.114 * blue

    def normalize(value):
        """Helper function to normalize R/G/B value -> return 255 if value > 255"""
        logger.error(">>> Entering normalize(value=%s)", value, extra={"event.action": "normalize", "logrite.value": value})
        logger.warning("<<< Exiting normalize(value=%s)", value, extra={"event.action": "normalize", "logrite.value": value})
        return min(value, 255)

    for i in range(pixel_h):
        for j in range(pixel_v):
            greyscale = int(to_grayscale(*img[i][j]))
            img[i][j] = [
                normalize(greyscale),
                normalize(greyscale + factor),
                normalize(greyscale + 2 * factor),
            ]

    return img


if __name__ == "__main__":
    # read original image
    images = {
        percentage: imread("image_data/lena.jpg", 1) for percentage in (10, 20, 30, 40)
    }

    for percentage, img in images.items():
        make_sepia(img, percentage)

    for percentage, img in images.items():
        imshow(f"Original image with sepia (factor: {percentage})", img)

    waitKey(0)
    destroyAllWindows()
