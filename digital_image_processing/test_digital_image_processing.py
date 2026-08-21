"""
PyTest's for Digital Image Processing
"""

import numpy as np
from cv2 import COLOR_BGR2GRAY, cvtColor, imread
from numpy import array, uint8
from PIL import Image

from digital_image_processing import change_contrast as cc
from digital_image_processing import convert_to_negative as cn
from digital_image_processing import sepia as sp
from digital_image_processing.dithering import burkes as bs
from digital_image_processing.edge_detection import canny
from digital_image_processing.filters import convolve as conv
from digital_image_processing.filters import gaussian_filter as gg
from digital_image_processing.filters import local_binary_pattern as lbp
from digital_image_processing.filters import median_filter as med
from digital_image_processing.filters import sobel_filter as sob
from digital_image_processing.resize import resize as rs
import logging
logger = logging.getLogger(__name__)

img = imread(r"digital_image_processing/image_data/lena_small.jpg")
gray = cvtColor(img, COLOR_BGR2GRAY)


# Test: convert_to_negative()
def test_convert_to_negative():
    logger.debug(">>> Entering test_convert_to_negative()")
    negative_img = cn.convert_to_negative(img)
    logger.debug("test_convert_to_negative(): negative_img → %s", negative_img)
    # assert negative_img array for at least one True
    assert negative_img.any()
    logger.debug("<<< Exiting test_convert_to_negative()")


# Test: change_contrast()
def test_change_contrast():
    logger.debug(">>> Entering test_change_contrast()")
    with Image.open("digital_image_processing/image_data/lena_small.jpg") as img:
        logger.error("Exception in test_change_contrast()", exc_info=True)
        # Work around assertion for response
        assert str(cc.change_contrast(img, 110)).startswith(
            "<PIL.Image.Image image mode=RGB size=100x100 at"
        )
        logger.debug("<<< Exiting test_change_contrast()")


# canny.gen_gaussian_kernel()
def test_gen_gaussian_kernel():
    logger.debug(">>> Entering test_gen_gaussian_kernel()")
    resp = canny.gen_gaussian_kernel(9, sigma=1.4)
    logger.debug("test_gen_gaussian_kernel(): resp → %s", resp)
    # Assert ambiguous array
    assert resp.all()
    logger.debug("<<< Exiting test_gen_gaussian_kernel()")


# canny.py
def test_canny():
    logger.debug(">>> Entering test_canny()")
    canny_img = imread("digital_image_processing/image_data/lena_small.jpg", 0)
    logger.debug("test_canny(): canny_img → %s", canny_img)
    # assert ambiguous array for all == True
    assert canny_img.all()
    canny_array = canny.canny(canny_img)
    logger.debug("test_canny(): canny_array → %s", canny_array)
    # assert canny array for at least one True
    assert canny_array.any()
    logger.debug("<<< Exiting test_canny()")


# filters/gaussian_filter.py
def test_gen_gaussian_kernel_filter():
    logger.debug(">>> Entering test_gen_gaussian_kernel_filter()")
    assert gg.gaussian_filter(gray, 5, sigma=0.9).all()
    logger.debug("<<< Exiting test_gen_gaussian_kernel_filter()")


def test_convolve_filter():
    logger.debug(">>> Entering test_convolve_filter()")
    # laplace diagonals
    laplace = array([[0.25, 0.5, 0.25], [0.5, -3, 0.5], [0.25, 0.5, 0.25]])
    logger.debug("test_convolve_filter(): laplace → %s", laplace)
    res = conv.img_convolve(gray, laplace).astype(uint8)
    logger.debug("test_convolve_filter(): res → %s", res)
    assert res.any()
    logger.debug("<<< Exiting test_convolve_filter()")


def test_median_filter():
    logger.debug(">>> Entering test_median_filter()")
    assert med.median_filter(gray, 3).any()
    logger.debug("<<< Exiting test_median_filter()")


def test_sobel_filter():
    logger.debug(">>> Entering test_sobel_filter()")
    grad, theta = sob.sobel_filter(gray)
    assert grad.any()
    assert theta.any()
    logger.debug("<<< Exiting test_sobel_filter()")


def test_sepia():
    logger.debug(">>> Entering test_sepia()")
    sepia = sp.make_sepia(img, 20)
    logger.debug("test_sepia(): sepia → %s", sepia)
    assert sepia.all()
    logger.debug("<<< Exiting test_sepia()")


def test_burkes(file_path: str = "digital_image_processing/image_data/lena_small.jpg"):
    logger.debug(">>> Entering test_burkes(file_path=%s)", file_path)
    burkes = bs.Burkes(imread(file_path, 1), 120)
    logger.debug("test_burkes(file_path=%s): burkes → %s", file_path, burkes)
    burkes.process()
    assert burkes.output_img.any()
    logger.debug("<<< Exiting test_burkes(file_path=%s)", file_path)


def test_nearest_neighbour(
    file_path: str = "digital_image_processing/image_data/lena_small.jpg",
):
    nn = rs.NearestNeighbour(imread(file_path, 1), 400, 200)
    nn.process()
    assert nn.output.any()


def test_local_binary_pattern():
    logger.debug(">>> Entering test_local_binary_pattern()")
    # pull request 10161 before:
    # "digital_image_processing/image_data/lena.jpg"
    # after: "digital_image_processing/image_data/lena_small.jpg"

    from os import getenv  # Speed up our Continuous Integration tests

    file_name = "lena_small.jpg" if getenv("CI") else "lena.jpg"
    logger.debug("test_local_binary_pattern(): file_name → %s", file_name)
    file_path = f"digital_image_processing/image_data/{file_name}"
    logger.debug("test_local_binary_pattern(): file_path → %s", file_path)

    # Reading the image and converting it to grayscale
    image = imread(file_path, 0)
    logger.debug("test_local_binary_pattern(): image → %s", image)

    # Test for get_neighbors_pixel function() return not None
    x_coordinate = 0
    logger.debug("test_local_binary_pattern(): x_coordinate → %s", x_coordinate)
    y_coordinate = 0
    logger.debug("test_local_binary_pattern(): y_coordinate → %s", y_coordinate)
    center = image[x_coordinate][y_coordinate]
    logger.debug("test_local_binary_pattern(): center → %s", center)

    neighbors_pixels = lbp.get_neighbors_pixel(
        image, x_coordinate, y_coordinate, center
    )

    assert neighbors_pixels is not None

    # Test for local_binary_pattern function()
    # Create a numpy array as the same height and width of read image
    lbp_image = np.zeros((image.shape[0], image.shape[1]))
    logger.debug("test_local_binary_pattern(): lbp_image → %s", lbp_image)

    # Iterating through the image and calculating the local binary pattern value
    # for each pixel.
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            lbp_image[i][j] = lbp.local_binary_value(image, i, j)

    logger.debug("<<< Exiting test_local_binary_pattern()")
    assert lbp_image.any()
