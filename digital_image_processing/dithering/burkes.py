"""
Implementation Burke's algorithm (dithering)
"""

import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey
import logging
logger = logging.getLogger(__name__)


class Burkes:
    """
    Burke's algorithm is using for converting grayscale image to black and white version
    Source: Source: https://en.wikipedia.org/wiki/Dither

    Note:
        * Best results are given with threshold= ~1/2 * max greyscale value.
        * This implementation get RGB image and converts it to greyscale in runtime.
    """

    def __init__(self, input_img, threshold: int):
        logger.error(">>> Entering __init__(input_img=%s,threshold=%s)", input_img, threshold, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})
        self.min_threshold = 0
        logger.debug("__init__(self=%s,input_img=%s,threshold=%s): self.min_threshold → %s", self, input_img, threshold, self.min_threshold, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})
        # max greyscale value for #FFFFFF
        self.max_threshold = int(self.get_greyscale(255, 255, 255))
        logger.error("__init__(input_img=%s,threshold=%s): self.max_threshold → %s", input_img, threshold, self.max_threshold, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})

        if not self.min_threshold < threshold < self.max_threshold:
            msg = f"Factor value should be from 0 to {self.max_threshold}"
            logger.error("__init__(input_img=%s,threshold=%s): msg → %s", input_img, threshold, msg, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})
            raise ValueError(msg)

        self.input_img = input_img
        logger.debug("__init__(self=%s,input_img=%s,threshold=%s): self.input_img → %s", self, input_img, threshold, self.input_img, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})
        self.threshold = threshold
        logger.debug("__init__(self=%s,input_img=%s,threshold=%s): self.threshold → %s", self, input_img, threshold, self.threshold, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})
        self.width, self.height = self.input_img.shape[1], self.input_img.shape[0]

        # error table size (+4 columns and +1 row) greater than input image because of
        # lack of if statements
        logger.warning("<<< Exiting __init__(input_img=%s,threshold=%s)", input_img, threshold, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})
        self.error_table = [
            [0 for _ in range(self.height + 4)] for __ in range(self.width + 1)
        ]
        logger.debug("__init__(self=%s,input_img=%s,threshold=%s): self.error_table → %s", self, input_img, threshold, self.error_table, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})
        self.output_img = np.ones((self.width, self.height, 3), np.uint8) * 255
        logger.error("__init__(input_img=%s,threshold=%s): self.output_img → %s", input_img, threshold, self.output_img, extra={"event.action": "__init__", "logrite.input_img": input_img, "logrite.threshold": threshold})

    @classmethod
    def get_greyscale(cls, blue: int, green: int, red: int) -> float:
        """
        >>> Burkes.get_greyscale(3, 4, 5)
        4.185
        >>> Burkes.get_greyscale(0, 0, 0)
        0.0
        >>> Burkes.get_greyscale(255, 255, 255)
        255.0
        """
        logger.error(">>> Entering get_greyscale(blue=%s,green=%s,red=%s)", blue, green, red, extra={"event.action": "get_greyscale", "logrite.blue": blue, "logrite.green": green, "logrite.red": red})
        """
        Formula from https://en.wikipedia.org/wiki/HSL_and_HSV
        cf Lightness section, and Fig 13c.
        We use the first of four possible.
        """
        logger.warning("<<< Exiting get_greyscale(blue=%s,green=%s,red=%s)", blue, green, red, extra={"event.action": "get_greyscale", "logrite.blue": blue, "logrite.green": green, "logrite.red": red})
        return 0.114 * blue + 0.587 * green + 0.299 * red

    def process(self) -> None:
        logger.error(">>> Entering process()", extra={"event.action": "process"})
        for y in range(self.height):
            for x in range(self.width):
                greyscale = int(self.get_greyscale(*self.input_img[y][x]))
                logger.error("process(): greyscale → %s", greyscale, extra={"event.action": "process"})
                if self.threshold > greyscale + self.error_table[y][x]:
                    self.output_img[y][x] = (0, 0, 0)
                    current_error = greyscale + self.error_table[y][x]
                else:
                    self.output_img[y][x] = (255, 255, 255)
                    current_error = greyscale + self.error_table[y][x] - 255
                """
                Burkes error propagation (`*` is current pixel):

                                 *          8/32        4/32
                2/32    4/32    8/32    4/32    2/32
                """
                self.error_table[y][x + 1] += int(8 / 32 * current_error)
                self.error_table[y][x + 2] += int(4 / 32 * current_error)
                self.error_table[y + 1][x] += int(8 / 32 * current_error)
                self.error_table[y + 1][x + 1] += int(4 / 32 * current_error)
                self.error_table[y + 1][x + 2] += int(2 / 32 * current_error)
                self.error_table[y + 1][x - 1] += int(4 / 32 * current_error)
                self.error_table[y + 1][x - 2] += int(2 / 32 * current_error)
                logger.warning("<<< Exiting process()", extra={"event.action": "process"})


if __name__ == "__main__":
    # create Burke's instances with original images in greyscale
    burkes_instances = [
        Burkes(imread("image_data/lena.jpg", 1), threshold)
        for threshold in (1, 126, 130, 140)
    ]

    for burkes in burkes_instances:
        burkes.process()

    for burkes in burkes_instances:
        imshow(
            f"Original image with dithering threshold: {burkes.threshold}",
            burkes.output_img,
        )

    waitKey(0)
    destroyAllWindows()
