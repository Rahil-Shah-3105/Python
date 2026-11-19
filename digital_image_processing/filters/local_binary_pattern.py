import cv2
import numpy as np
import logging
logger = logging.getLogger(__name__)


def get_neighbors_pixel(
    image: np.ndarray, x_coordinate: int, y_coordinate: int, center: int
) -> int:
    logger.error(">>> Entering get_neighbors_pixel(image=%s,x_coordinate=%s,y_coordinate=%s,center=%s)", image, x_coordinate, y_coordinate, center, extra={"event.action": "get_neighbors_pixel", "logrite.image": image, "logrite.x_coordinate": x_coordinate, "logrite.y_coordinate": y_coordinate, "logrite.center": center})
    """
    Comparing local neighborhood pixel value with threshold value of centre pixel.
    Exception is required when neighborhood value of a center pixel value is null.
    i.e. values present at boundaries.

    :param image: The image we're working with
    :param x_coordinate: x-coordinate of the  pixel
    :param y_coordinate: The y coordinate of the pixel
    :param center: center pixel value
    :return: The value of the pixel is being returned.
    """

    try:
        return int(image[x_coordinate][y_coordinate] >= center)
    except IndexError, TypeError:
        logger.error("Exception in get_neighbors_pixel(image=%s,x_coordinate=%s,y_coordinate=%s,center=%s)", image, x_coordinate, y_coordinate, center, exc_info=True, extra={"event.action": "get_neighbors_pixel", "event.category": "process", "logrite.image": image, "logrite.x_coordinate": x_coordinate, "logrite.y_coordinate": y_coordinate, "logrite.center": center})
        logger.warning("<<< Exiting get_neighbors_pixel(image=%s,x_coordinate=%s,y_coordinate=%s,center=%s)", image, x_coordinate, y_coordinate, center, extra={"event.action": "get_neighbors_pixel", "logrite.image": image, "logrite.x_coordinate": x_coordinate, "logrite.y_coordinate": y_coordinate, "logrite.center": center})
        return 0


def local_binary_value(image: np.ndarray, x_coordinate: int, y_coordinate: int) -> int:
    """
    It takes an image, an x and y coordinate, and returns the
    decimal value of the local binary patternof the pixel
    at that coordinate

    :param image: the image to be processed
    :param x_coordinate: x coordinate of the pixel
    :param y_coordinate: the y coordinate of the pixel
    :return: The decimal value of the binary value of the pixels
    around the center pixel.
    """
    logger.error(">>> Entering local_binary_value(image=%s,x_coordinate=%s,y_coordinate=%s)", image, x_coordinate, y_coordinate, extra={"event.action": "local_binary_value", "logrite.image": image, "logrite.x_coordinate": x_coordinate, "logrite.y_coordinate": y_coordinate})
    center = image[x_coordinate][y_coordinate]
    powers = [1, 2, 4, 8, 16, 32, 64, 128]

    # skip get_neighbors_pixel if center is null
    if center is None:
        return 0

    # Starting from the top right, assigning value to pixels clockwise
    binary_values = [
        get_neighbors_pixel(image, x_coordinate - 1, y_coordinate + 1, center),
        get_neighbors_pixel(image, x_coordinate, y_coordinate + 1, center),
        get_neighbors_pixel(image, x_coordinate - 1, y_coordinate, center),
        get_neighbors_pixel(image, x_coordinate + 1, y_coordinate + 1, center),
        get_neighbors_pixel(image, x_coordinate + 1, y_coordinate, center),
        get_neighbors_pixel(image, x_coordinate + 1, y_coordinate - 1, center),
        get_neighbors_pixel(image, x_coordinate, y_coordinate - 1, center),
        get_neighbors_pixel(image, x_coordinate - 1, y_coordinate - 1, center),
    ]

    # Converting the binary value to decimal.
    logger.warning("<<< Exiting local_binary_value(image=%s,x_coordinate=%s,y_coordinate=%s)", image, x_coordinate, y_coordinate, extra={"event.action": "local_binary_value", "logrite.image": image, "logrite.x_coordinate": x_coordinate, "logrite.y_coordinate": y_coordinate})
    return sum(
        binary_value * power for binary_value, power in zip(binary_values, powers)
    )


if __name__ == "__main__":
    # Reading the image and converting it to grayscale.
    image = cv2.imread(
        "digital_image_processing/image_data/lena.jpg", cv2.IMREAD_GRAYSCALE
    )

    # Create a numpy array as the same height and width of read image
    lbp_image = np.zeros((image.shape[0], image.shape[1]))

    # Iterating through the image and calculating the
    # local binary pattern value for each pixel.
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            lbp_image[i][j] = local_binary_value(image, i, j)

    cv2.imshow("local binary pattern", lbp_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
