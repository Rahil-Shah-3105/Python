"""Multiple image resizing techniques"""

import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey
import logging
logger = logging.getLogger(__name__)


class NearestNeighbour:
    """
    Simplest and fastest version of image resizing.
    Source: https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation
    """

    def __init__(self, img, dst_width: int, dst_height: int):
        logger.debug(">>> Entering __init__(img=%s,dst_width=%s,dst_height=%s)", img, dst_width, dst_height)
        if dst_width < 0 or dst_height < 0:
            raise ValueError("Destination width/height should be > 0")

        self.img = img
        logger.debug("__init__(self=%s,img=%s,dst_width=%s,dst_height=%s): self.img → %s", self, img, dst_width, dst_height, self.img)
        self.src_w = img.shape[1]
        logger.debug("__init__(self=%s,img=%s,dst_width=%s,dst_height=%s): self.src_w → %s", self, img, dst_width, dst_height, self.src_w)
        self.src_h = img.shape[0]
        logger.debug("__init__(self=%s,img=%s,dst_width=%s,dst_height=%s): self.src_h → %s", self, img, dst_width, dst_height, self.src_h)
        self.dst_w = dst_width
        logger.debug("__init__(self=%s,img=%s,dst_width=%s,dst_height=%s): self.dst_w → %s", self, img, dst_width, dst_height, self.dst_w)
        self.dst_h = dst_height
        logger.debug("__init__(self=%s,img=%s,dst_width=%s,dst_height=%s): self.dst_h → %s", self, img, dst_width, dst_height, self.dst_h)

        self.ratio_x = self.src_w / self.dst_w
        logger.debug("__init__(self=%s,img=%s,dst_width=%s,dst_height=%s): self.ratio_x → %s", self, img, dst_width, dst_height, self.ratio_x)
        self.ratio_y = self.src_h / self.dst_h
        logger.debug("__init__(self=%s,img=%s,dst_width=%s,dst_height=%s): self.ratio_y → %s", self, img, dst_width, dst_height, self.ratio_y)

        self.output = self.output_img = (
            np.ones((self.dst_h, self.dst_w, 3), np.uint8) * 255
        )
        logger.debug("<<< Exiting __init__(img=%s,dst_width=%s,dst_height=%s)", img, dst_width, dst_height)

    def process(self):
        logger.debug(">>> Entering process()")
        for i in range(self.dst_h):
            for j in range(self.dst_w):
                self.output[i][j] = self.img[self.get_y(i)][self.get_x(j)]
                logger.debug("<<< Exiting process()")

    def get_x(self, x: int) -> int:
        """
        Get parent X coordinate for destination X
        :param x: Destination X coordinate
        :return: Parent X coordinate based on `x ratio`
        >>> nn = NearestNeighbour(imread("digital_image_processing/image_data/lena.jpg",
        ...                              1), 100, 100)
        >>> nn.ratio_x = 0.5
        >>> nn.get_x(4)
        2
        """
        logger.debug(">>> Entering get_x(x=%s)", x)
        logger.debug("<<< Exiting get_x(x=%s)", x)
        return int(self.ratio_x * x)

    def get_y(self, y: int) -> int:
        """
        Get parent Y coordinate for destination Y
        :param y: Destination X coordinate
        :return: Parent X coordinate based on `y ratio`
        >>> nn = NearestNeighbour(imread("digital_image_processing/image_data/lena.jpg",
        ...                              1), 100, 100)
        >>> nn.ratio_y = 0.5
        >>> nn.get_y(4)
        2
        """
        logger.debug(">>> Entering get_y(y=%s)", y)
        logger.debug("<<< Exiting get_y(y=%s)", y)
        return int(self.ratio_y * y)


if __name__ == "__main__":
    dst_w, dst_h = 800, 600
    im = imread("image_data/lena.jpg", 1)
    n = NearestNeighbour(im, dst_w, dst_h)
    n.process()

    imshow(
        f"Image resized from: {im.shape[1]}x{im.shape[0]} to {dst_w}x{dst_h}", n.output
    )
    waitKey(0)
    destroyAllWindows()
