"""
Implementation of gaussian filter algorithm
"""

from itertools import product

from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import dot, exp, mgrid, pi, ravel, square, uint8, zeros
import logging
logger = logging.getLogger(__name__)


def gen_gaussian_kernel(k_size, sigma):
    logger.error(">>> Entering gen_gaussian_kernel(k_size=%s,sigma=%s)", k_size, sigma, extra={"event.action": "gen_gaussian_kernel", "logrite.k_size": k_size, "logrite.sigma": sigma})
    center = k_size // 2
    x, y = mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = 1 / (2 * pi * sigma) * exp(-(square(x) + square(y)) / (2 * square(sigma)))
    logger.error("gen_gaussian_kernel(k_size=%s,sigma=%s): g → %s", k_size, sigma, g, extra={"event.action": "gen_gaussian_kernel", "logrite.k_size": k_size, "logrite.sigma": sigma})
    logger.warning("<<< Exiting gen_gaussian_kernel(k_size=%s,sigma=%s)", k_size, sigma, extra={"event.action": "gen_gaussian_kernel", "logrite.k_size": k_size, "logrite.sigma": sigma})
    return g


def gaussian_filter(image, k_size, sigma):
    logger.error(">>> Entering gaussian_filter(image=%s,k_size=%s,sigma=%s)", image, k_size, sigma, extra={"event.action": "gaussian_filter", "logrite.image": image, "logrite.k_size": k_size, "logrite.sigma": sigma})
    height, width = image.shape[0], image.shape[1]
    # dst image height and width
    dst_height = height - k_size + 1
    dst_width = width - k_size + 1

    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = zeros((dst_height * dst_width, k_size * k_size))
    logger.error("gaussian_filter(image=%s,k_size=%s,sigma=%s): image_array → %s", image, k_size, sigma, image_array, extra={"event.action": "gaussian_filter", "logrite.image": image, "logrite.k_size": k_size, "logrite.sigma": sigma})
    for row, (i, j) in enumerate(product(range(dst_height), range(dst_width))):
        window = ravel(image[i : i + k_size, j : j + k_size])
        logger.error("gaussian_filter(image=%s,k_size=%s,sigma=%s): window → %s", image, k_size, sigma, window, extra={"event.action": "gaussian_filter", "logrite.image": image, "logrite.k_size": k_size, "logrite.sigma": sigma})
        image_array[row, :] = window

    #  turn the kernel into shape(k*k, 1)
    gaussian_kernel = gen_gaussian_kernel(k_size, sigma)
    logger.error("gaussian_filter(image=%s,k_size=%s,sigma=%s): gaussian_kernel → %s", image, k_size, sigma, gaussian_kernel, extra={"event.action": "gaussian_filter", "logrite.image": image, "logrite.k_size": k_size, "logrite.sigma": sigma})
    filter_array = ravel(gaussian_kernel)
    logger.error("gaussian_filter(image=%s,k_size=%s,sigma=%s): filter_array → %s", image, k_size, sigma, filter_array, extra={"event.action": "gaussian_filter", "logrite.image": image, "logrite.k_size": k_size, "logrite.sigma": sigma})

    # reshape and get the dst image
    dst = dot(image_array, filter_array).reshape(dst_height, dst_width).astype(uint8)
    logger.error("gaussian_filter(image=%s,k_size=%s,sigma=%s): dst → %s", image, k_size, sigma, dst, extra={"event.action": "gaussian_filter", "logrite.image": image, "logrite.k_size": k_size, "logrite.sigma": sigma})

    logger.warning("<<< Exiting gaussian_filter(image=%s,k_size=%s,sigma=%s)", image, k_size, sigma, extra={"event.action": "gaussian_filter", "logrite.image": image, "logrite.k_size": k_size, "logrite.sigma": sigma})
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
