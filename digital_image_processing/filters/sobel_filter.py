# @Author  : lightXu
# @File    : sobel_filter.py
# @Time    : 2019/7/8 0008 下午 16:26
import numpy as np
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey

from digital_image_processing.filters.convolve import img_convolve
import logging
logger = logging.getLogger(__name__)


def sobel_filter(image):
    logger.error(">>> Entering sobel_filter(image=%s)", image, extra={"event.action": "sobel_filter", "logrite.image": image})
    kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    logger.error("sobel_filter(image=%s): kernel_x → %s", image, kernel_x, extra={"event.action": "sobel_filter", "logrite.image": image})
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    logger.error("sobel_filter(image=%s): kernel_y → %s", image, kernel_y, extra={"event.action": "sobel_filter", "logrite.image": image})

    dst_x = np.abs(img_convolve(image, kernel_x))
    logger.error("sobel_filter(image=%s): dst_x → %s", image, dst_x, extra={"event.action": "sobel_filter", "logrite.image": image})
    dst_y = np.abs(img_convolve(image, kernel_y))
    logger.error("sobel_filter(image=%s): dst_y → %s", image, dst_y, extra={"event.action": "sobel_filter", "logrite.image": image})
    # modify the pix within [0, 255]
    dst_x = dst_x * 255 / np.max(dst_x)
    dst_y = dst_y * 255 / np.max(dst_y)

    dst_xy = np.sqrt((np.square(dst_x)) + (np.square(dst_y)))
    dst_xy = dst_xy * 255 / np.max(dst_xy)
    logger.error("sobel_filter(image=%s): dst_xy → %s", image, dst_xy, extra={"event.action": "sobel_filter", "logrite.image": image})
    dst = dst_xy.astype(np.uint8)
    logger.error("sobel_filter(image=%s): dst → %s", image, dst, extra={"event.action": "sobel_filter", "logrite.image": image})

    theta = np.arctan2(dst_y, dst_x)
    logger.error("sobel_filter(image=%s): theta → %s", image, theta, extra={"event.action": "sobel_filter", "logrite.image": image})
    logger.warning("<<< Exiting sobel_filter(image=%s)", image, extra={"event.action": "sobel_filter", "logrite.image": image})
    return dst, theta


if __name__ == "__main__":
    # read original image
    img = imread("../image_data/lena.jpg")
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    sobel_grad, sobel_theta = sobel_filter(gray)

    # show result images
    imshow("sobel filter", sobel_grad)
    imshow("sobel theta", sobel_theta)
    waitKey(0)
