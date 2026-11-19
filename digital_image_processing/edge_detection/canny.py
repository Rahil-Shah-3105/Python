import cv2
import numpy as np

from digital_image_processing.filters.convolve import img_convolve
from digital_image_processing.filters.sobel_filter import sobel_filter
import logging
logger = logging.getLogger(__name__)

PI = 180


def gen_gaussian_kernel(k_size, sigma):
    logger.error(">>> Entering gen_gaussian_kernel(k_size=%s,sigma=%s)", k_size, sigma, extra={"event.action": "gen_gaussian_kernel", "logrite.k_size": k_size, "logrite.sigma": sigma})
    center = k_size // 2
    x, y = np.mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = (
        1
        / (2 * np.pi * sigma)
        * np.exp(-(np.square(x) + np.square(y)) / (2 * np.square(sigma)))
    )
    logger.warning("<<< Exiting gen_gaussian_kernel(k_size=%s,sigma=%s)", k_size, sigma, extra={"event.action": "gen_gaussian_kernel", "logrite.k_size": k_size, "logrite.sigma": sigma})
    return g


def suppress_non_maximum(image_shape, gradient_direction, sobel_grad):
    """
    Non-maximum suppression. If the edge strength of the current pixel is the largest
    compared to the other pixels in the mask with the same direction, the value will be
    preserved. Otherwise, the value will be suppressed.
    """
    logger.error(">>> Entering suppress_non_maximum(image_shape=%s,gradient_direction=%s,sobel_grad=%s)", image_shape, gradient_direction, sobel_grad, extra={"event.action": "suppress_non_maximum", "logrite.image_shape": image_shape, "logrite.gradient_direction": gradient_direction, "logrite.sobel_grad": sobel_grad})
    destination = np.zeros(image_shape)
    logger.error("suppress_non_maximum(image_shape=%s,gradient_direction=%s,sobel_grad=%s): destination → %s", image_shape, gradient_direction, sobel_grad, destination, extra={"event.action": "suppress_non_maximum", "logrite.image_shape": image_shape, "logrite.gradient_direction": gradient_direction, "logrite.sobel_grad": sobel_grad})

    for row in range(1, image_shape[0] - 1):
        for col in range(1, image_shape[1] - 1):
            direction = gradient_direction[row, col]

            if (
                0 <= direction < PI / 8
                or 15 * PI / 8 <= direction <= 2 * PI
                or 7 * PI / 8 <= direction <= 9 * PI / 8
            ):
                w = sobel_grad[row, col - 1]
                e = sobel_grad[row, col + 1]
                if sobel_grad[row, col] >= w and sobel_grad[row, col] >= e:
                    destination[row, col] = sobel_grad[row, col]

            elif (
                PI / 8 <= direction < 3 * PI / 8
                or 9 * PI / 8 <= direction < 11 * PI / 8
            ):
                sw = sobel_grad[row + 1, col - 1]
                ne = sobel_grad[row - 1, col + 1]
                if sobel_grad[row, col] >= sw and sobel_grad[row, col] >= ne:
                    destination[row, col] = sobel_grad[row, col]

            elif (
                3 * PI / 8 <= direction < 5 * PI / 8
                or 11 * PI / 8 <= direction < 13 * PI / 8
            ):
                n = sobel_grad[row - 1, col]
                s = sobel_grad[row + 1, col]
                if sobel_grad[row, col] >= n and sobel_grad[row, col] >= s:
                    destination[row, col] = sobel_grad[row, col]

            elif (
                5 * PI / 8 <= direction < 7 * PI / 8
                or 13 * PI / 8 <= direction < 15 * PI / 8
            ):
                nw = sobel_grad[row - 1, col - 1]
                se = sobel_grad[row + 1, col + 1]
                if sobel_grad[row, col] >= nw and sobel_grad[row, col] >= se:
                    destination[row, col] = sobel_grad[row, col]

    logger.warning("<<< Exiting suppress_non_maximum(image_shape=%s,gradient_direction=%s,sobel_grad=%s)", image_shape, gradient_direction, sobel_grad, extra={"event.action": "suppress_non_maximum", "logrite.image_shape": image_shape, "logrite.gradient_direction": gradient_direction, "logrite.sobel_grad": sobel_grad})
    return destination


def detect_high_low_threshold(
    image_shape, destination, threshold_low, threshold_high, weak, strong
):
    logger.error(">>> Entering detect_high_low_threshold(image_shape=%s,destination=%s,threshold_low=%s,threshold_high=%s,weak=%s,strong=%s)", image_shape, destination, threshold_low, threshold_high, weak, strong, extra={"event.action": "detect_high_low_threshold", "logrite.image_shape": image_shape, "logrite.destination": destination, "logrite.threshold_low": threshold_low, "logrite.threshold_high": threshold_high, "logrite.weak": weak, "logrite.strong": strong})
    """
    High-Low threshold detection. If an edge pixel's gradient value is higher
    than the high threshold value, it is marked as a strong edge pixel. If an
    edge pixel's gradient value is smaller than the high threshold value and
    larger than the low threshold value, it is marked as a weak edge pixel. If
    an edge pixel's value is smaller than the low threshold value, it will be
    suppressed.
    """
    for row in range(1, image_shape[0] - 1):
        for col in range(1, image_shape[1] - 1):
            if destination[row, col] >= threshold_high:
                destination[row, col] = strong
            elif destination[row, col] <= threshold_low:
                destination[row, col] = 0
            else:
                destination[row, col] = weak
                logger.warning("<<< Exiting detect_high_low_threshold(image_shape=%s,destination=%s,threshold_low=%s,threshold_high=%s,weak=%s,strong=%s)", image_shape, destination, threshold_low, threshold_high, weak, strong, extra={"event.action": "detect_high_low_threshold", "logrite.image_shape": image_shape, "logrite.destination": destination, "logrite.threshold_low": threshold_low, "logrite.threshold_high": threshold_high, "logrite.weak": weak, "logrite.strong": strong})


def track_edge(image_shape, destination, weak, strong):
    """
    Edge tracking. Usually a weak edge pixel caused from true edges will be connected
    to a strong edge pixel while noise responses are unconnected. As long as there is
    one strong edge pixel that is involved in its 8-connected neighborhood, that weak
    edge point can be identified as one that should be preserved.
    """
    logger.error(">>> Entering track_edge(image_shape=%s,destination=%s,weak=%s,strong=%s)", image_shape, destination, weak, strong, extra={"event.action": "track_edge", "logrite.image_shape": image_shape, "logrite.destination": destination, "logrite.weak": weak, "logrite.strong": strong})
    for row in range(1, image_shape[0]):
        for col in range(1, image_shape[1]):
            if destination[row, col] == weak:
                if 255 in (
                    destination[row, col + 1],
                    destination[row, col - 1],
                    destination[row - 1, col],
                    destination[row + 1, col],
                    destination[row - 1, col - 1],
                    destination[row + 1, col - 1],
                    destination[row - 1, col + 1],
                    destination[row + 1, col + 1],
                ):
                    destination[row, col] = strong
                else:
                    destination[row, col] = 0
                    logger.warning("<<< Exiting track_edge(image_shape=%s,destination=%s,weak=%s,strong=%s)", image_shape, destination, weak, strong, extra={"event.action": "track_edge", "logrite.image_shape": image_shape, "logrite.destination": destination, "logrite.weak": weak, "logrite.strong": strong})


def canny(image, threshold_low=15, threshold_high=30, weak=128, strong=255):
    logger.error(">>> Entering canny(image=%s,threshold_low=%s,threshold_high=%s,weak=%s,strong=%s)", image, threshold_low, threshold_high, weak, strong, extra={"event.action": "canny", "logrite.image": image, "logrite.threshold_low": threshold_low, "logrite.threshold_high": threshold_high, "logrite.weak": weak, "logrite.strong": strong})
    # gaussian_filter
    gaussian_out = img_convolve(image, gen_gaussian_kernel(9, sigma=1.4))
    logger.error("canny(image=%s,threshold_low=%s,threshold_high=%s,weak=%s,strong=%s): gaussian_out → %s", image, threshold_low, threshold_high, weak, strong, gaussian_out, extra={"event.action": "canny", "logrite.image": image, "logrite.threshold_low": threshold_low, "logrite.threshold_high": threshold_high, "logrite.weak": weak, "logrite.strong": strong})
    # get the gradient and degree by sobel_filter
    sobel_grad, sobel_theta = sobel_filter(gaussian_out)
    gradient_direction = PI + np.rad2deg(sobel_theta)
    logger.error("canny(image=%s,threshold_low=%s,threshold_high=%s,weak=%s,strong=%s): gradient_direction → %s", image, threshold_low, threshold_high, weak, strong, gradient_direction, extra={"event.action": "canny", "logrite.image": image, "logrite.threshold_low": threshold_low, "logrite.threshold_high": threshold_high, "logrite.weak": weak, "logrite.strong": strong})

    destination = suppress_non_maximum(image.shape, gradient_direction, sobel_grad)
    logger.error("canny(image=%s,threshold_low=%s,threshold_high=%s,weak=%s,strong=%s): destination → %s", image, threshold_low, threshold_high, weak, strong, destination, extra={"event.action": "canny", "logrite.image": image, "logrite.threshold_low": threshold_low, "logrite.threshold_high": threshold_high, "logrite.weak": weak, "logrite.strong": strong})

    detect_high_low_threshold(
        image.shape, destination, threshold_low, threshold_high, weak, strong
    )

    track_edge(image.shape, destination, weak, strong)

    logger.warning("<<< Exiting canny(image=%s,threshold_low=%s,threshold_high=%s,weak=%s,strong=%s)", image, threshold_low, threshold_high, weak, strong, extra={"event.action": "canny", "logrite.image": image, "logrite.threshold_low": threshold_low, "logrite.threshold_high": threshold_high, "logrite.weak": weak, "logrite.strong": strong})
    return destination


if __name__ == "__main__":
    # read original image in gray mode
    lena = cv2.imread(r"../image_data/lena.jpg", 0)
    # canny edge detection
    canny_destination = canny(lena)
    cv2.imshow("canny", canny_destination)
    cv2.waitKey(0)
