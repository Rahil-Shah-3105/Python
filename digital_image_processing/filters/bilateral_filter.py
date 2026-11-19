"""
Implementation of Bilateral filter

Inputs:
    img: A 2d image with values in between 0 and 1
    varS: variance in space dimension.
    varI: variance in Intensity.
    N: Kernel size(Must be an odd number)
Output:
    img:A 2d zero padded image with values in between 0 and 1
"""

import math
import sys

import cv2
import numpy as np
import logging
logger = logging.getLogger(__name__)


def vec_gaussian(img: np.ndarray, variance: float) -> np.ndarray:
    logger.error(">>> Entering vec_gaussian(img=%s,variance=%s)", img, variance, extra={"event.action": "vec_gaussian", "logrite.img": img, "logrite.variance": variance})
    # For applying gaussian function for each element in matrix.
    sigma = math.sqrt(variance)
    logger.error("vec_gaussian(img=%s,variance=%s): sigma → %s", img, variance, sigma, extra={"event.action": "vec_gaussian", "logrite.img": img, "logrite.variance": variance})
    cons = 1 / (sigma * math.sqrt(2 * math.pi))
    logger.error("vec_gaussian(img=%s,variance=%s): cons → %s", img, variance, cons, extra={"event.action": "vec_gaussian", "logrite.img": img, "logrite.variance": variance})
    logger.warning("<<< Exiting vec_gaussian(img=%s,variance=%s)", img, variance, extra={"event.action": "vec_gaussian", "logrite.img": img, "logrite.variance": variance})
    return cons * np.exp(-((img / sigma) ** 2) * 0.5)


def get_slice(img: np.ndarray, x: int, y: int, kernel_size: int) -> np.ndarray:
    logger.error(">>> Entering get_slice(img=%s,x=%s,y=%s,kernel_size=%s)", img, x, y, kernel_size, extra={"event.action": "get_slice", "logrite.img": img, "logrite.x": x, "logrite.y": y, "logrite.kernel_size": kernel_size})
    half = kernel_size // 2
    logger.warning("<<< Exiting get_slice(img=%s,x=%s,y=%s,kernel_size=%s)", img, x, y, kernel_size, extra={"event.action": "get_slice", "logrite.img": img, "logrite.x": x, "logrite.y": y, "logrite.kernel_size": kernel_size})
    return img[x - half : x + half + 1, y - half : y + half + 1]


def get_gauss_kernel(kernel_size: int, spatial_variance: float) -> np.ndarray:
    logger.error(">>> Entering get_gauss_kernel(kernel_size=%s,spatial_variance=%s)", kernel_size, spatial_variance, extra={"event.action": "get_gauss_kernel", "logrite.kernel_size": kernel_size, "logrite.spatial_variance": spatial_variance})
    # Creates a gaussian kernel of given dimension.
    arr = np.zeros((kernel_size, kernel_size))
    logger.error("get_gauss_kernel(kernel_size=%s,spatial_variance=%s): arr → %s", kernel_size, spatial_variance, arr, extra={"event.action": "get_gauss_kernel", "logrite.kernel_size": kernel_size, "logrite.spatial_variance": spatial_variance})
    for i in range(kernel_size):
        for j in range(kernel_size):
            arr[i, j] = math.sqrt(
                abs(i - kernel_size // 2) ** 2 + abs(j - kernel_size // 2) ** 2
            )
    return vec_gaussian(arr, spatial_variance)


def bilateral_filter(
    img: np.ndarray,
    spatial_variance: float,
    intensity_variance: float,
    kernel_size: int,
) -> np.ndarray:
    img2 = np.zeros(img.shape)
    gauss_ker = get_gauss_kernel(kernel_size, spatial_variance)
    size_x, size_y = img.shape
    for i in range(kernel_size // 2, size_x - kernel_size // 2):
        for j in range(kernel_size // 2, size_y - kernel_size // 2):
            img_s = get_slice(img, i, j, kernel_size)
            img_i = img_s - img_s[kernel_size // 2, kernel_size // 2]
            img_ig = vec_gaussian(img_i, intensity_variance)
            weights = np.multiply(gauss_ker, img_ig)
            vals = np.multiply(img_s, weights)
            val = np.sum(vals) / np.sum(weights)
            img2[i, j] = val
    return img2


def parse_args(args: list) -> tuple:
    filename = args[1] if args[1:] else "../image_data/lena.jpg"
    spatial_variance = float(args[2]) if args[2:] else 1.0
    intensity_variance = float(args[3]) if args[3:] else 1.0
    if args[4:]:
        kernel_size = int(args[4])
        kernel_size = kernel_size + abs(kernel_size % 2 - 1)
    else:
        kernel_size = 5
    return filename, spatial_variance, intensity_variance, kernel_size


if __name__ == "__main__":
    filename, spatial_variance, intensity_variance, kernel_size = parse_args(sys.argv)
    img = cv2.imread(filename, 0)
    cv2.imshow("input image", img)

    out = img / 255
    out = out.astype("float32")
    out = bilateral_filter(out, spatial_variance, intensity_variance, kernel_size)
    out = out * 255
    out = np.uint8(out)
    cv2.imshow("output image", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
