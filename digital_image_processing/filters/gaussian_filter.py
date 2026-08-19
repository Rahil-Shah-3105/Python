"""
Implementation of gaussian filter algorithm
"""

from itertools import product

from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import logging
logger = logging.getLogger(__name__)


def gen_gaussian_kernel(k_size, sigma):
    logger.debug(">>> Entering gen_gaussian_kernel(k_size=%s,sigma=%s)", k_size, sigma)
    center = k_size // 2
    logger.debug("gen_gaussian_kernel(k_size=%s,sigma=%s): center → %s", k_size, sigma, center)
    x, y = mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = 1 / (2 * pi * sigma) * exp(-(square(x) + square(y)) / (2 * square(sigma)))
    logger.debug("gen_gaussian_kernel(k_size=%s,sigma=%s): g → %s", k_size, sigma, g)
    logger.debug("<<< Exiting gen_gaussian_kernel(k_size=%s,sigma=%s)", k_size, sigma)
    return g


def gaussian_filter(image, k_size, sigma):
    logger.debug(">>> Entering gaussian_filter(image=%s,k_size=%s,sigma=%s)", image, k_size, sigma)
    height, width = image.shape[0], image.shape[1]
    # dst image height and width
    dst_height = height - k_size + 1
    logger.debug("gaussian_filter(image=%s,k_size=%s,sigma=%s): dst_height → %s", image, k_size, sigma, dst_height)
    dst_width = width - k_size + 1
    logger.debug("gaussian_filter(image=%s,k_size=%s,sigma=%s): dst_width → %s", image, k_size, sigma, dst_width)

    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = zeros((dst_height * dst_width, k_size * k_size))
    logger.debug("gaussian_filter(image=%s,k_size=%s,sigma=%s): image_array → %s", image, k_size, sigma, image_array)
    for row, (i, j) in enumerate(product(range(dst_height), range(dst_width))):
        window = ravel(image[i : i + k_size, j : j + k_size])
        logger.debug("gaussian_filter(image=%s,k_size=%s,sigma=%s): window → %s", image, k_size, sigma, window)
        image_array[row, :] = window

    #  turn the kernel into shape(k*k, 1)
    gaussian_kernel = gen_gaussian_kernel(k_size, sigma)
    logger.debug("gaussian_filter(image=%s,k_size=%s,sigma=%s): gaussian_kernel → %s", image, k_size, sigma, gaussian_kernel)
    filter_array = ravel(gaussian_kernel)
    logger.debug("gaussian_filter(image=%s,k_size=%s,sigma=%s): filter_array → %s", image, k_size, sigma, filter_array)

    # reshape and get the dst image
    dst = dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)
    logger.debug("gaussian_filter(image=%s,k_size=%s,sigma=%s): dst → %s", image, k_size, sigma, dst)

    logger.debug("<<< Exiting gaussian_filter(image=%s,k_size=%s,sigma=%s)", image, k_size, sigma)
    return dst


if __name__ == "__main__":
    # read original image
    img = imread(r"../image_data/lena.jpg")
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # get values with two different mask size
    gaussian3x3 = gaussian_filter(gray, 3, sigma=1)
    gaussian5x5 = gaussian_filter(gray, 5, sigma=0.8)

    # show result images
    imshow("gaussian filter with 3x3 mask", gaussian3x3)
    imshow("gaussian filter with 5x5 mask", gaussian5x5)
    waitKey()
