"""
Implementation of median filter algorithm
"""

from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import divide, int8, multiply, ravel, sort, zeros_like
import logging
logger = logging.getLogger(__name__)


def median_filter(gray_img, mask=3):
    """
    :param gray_img: gray image
    :param mask: mask size
    :return: image with median filter
    """
    logger.error(">>> Entering median_filter(gray_img=%s,mask=%s)", gray_img, mask, extra={"event.action": "median_filter", "logrite.gray_img": gray_img, "logrite.mask": mask})
    # set image borders
    bd = int(mask / 2)
    logger.error("median_filter(gray_img=%s,mask=%s): bd → %s", gray_img, mask, bd, extra={"event.action": "median_filter", "logrite.gray_img": gray_img, "logrite.mask": mask})
    # copy image size
    median_img = zeros_like(gray_img)
    logger.error("median_filter(gray_img=%s,mask=%s): median_img → %s", gray_img, mask, median_img, extra={"event.action": "median_filter", "logrite.gray_img": gray_img, "logrite.mask": mask})
    for i in range(bd, gray_img.shape[0] - bd):
        for j in range(bd, gray_img.shape[1] - bd):
            # get mask according with mask
            kernel = ravel(gray_img[i - bd : i + bd + 1, j - bd : j + bd + 1])
            logger.error("median_filter(gray_img=%s,mask=%s): kernel → %s", gray_img, mask, kernel, extra={"event.action": "median_filter", "logrite.gray_img": gray_img, "logrite.mask": mask})
            # calculate mask median
            median = sort(kernel)[int8(divide((multiply(mask, mask)), 2) + 1)]
            logger.error("median_filter(gray_img=%s,mask=%s): median → %s", gray_img, mask, median, extra={"event.action": "median_filter", "logrite.gray_img": gray_img, "logrite.mask": mask})
            median_img[i, j] = median
    logger.warning("<<< Exiting median_filter(gray_img=%s,mask=%s)", gray_img, mask, extra={"event.action": "median_filter", "logrite.gray_img": gray_img, "logrite.mask": mask})
    return median_img


if __name__ == "__main__":
    # read original image
    img = imread("../image_data/lena.jpg")
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # get values with two different mask size
    median3x3 = median_filter(gray, 3)
    median5x5 = median_filter(gray, 5)

    # show result images
    imshow("median filter with 3x3 mask", median3x3)
    imshow("median filter with 5x5 mask", median5x5)
    waitKey(0)
