# @Author  : lightXu
# @File    : convolve.py
# @Time    : 2019/7/8 0008 下午 16:13
from cv2 import COLOR_BGR2GRAY, cvtColor, imread, imshow, waitKey
from numpy import array, dot, pad, ravel, uint8, zeros
import logging
logger = logging.getLogger(__name__)


def im2col(image, block_size):
    logger.debug(">>> Entering im2col(image=%s,block_size=%s)", image, block_size)
    rows, cols = image.shape
    dst_height = cols - block_size[1] + 1
    logger.debug("im2col(image=%s,block_size=%s): dst_height → %s", image, block_size, dst_height)
    dst_width = rows - block_size[0] + 1
    logger.debug("im2col(image=%s,block_size=%s): dst_width → %s", image, block_size, dst_width)
    image_array = zeros((dst_height * dst_width, block_size[1] * block_size[0]))
    logger.debug("im2col(image=%s,block_size=%s): image_array → %s", image, block_size, image_array)
    row = 0
    logger.debug("im2col(image=%s,block_size=%s): row → %s", image, block_size, row)
    for i in range(dst_height):
        for j in range(dst_width):
            window = ravel(image[i : i + block_size[0], j : j + block_size[1]])
            logger.debug("im2col(image=%s,block_size=%s): window → %s", image, block_size, window)
            image_array[row, :] = window
            row += 1

    logger.debug("<<< Exiting im2col(image=%s,block_size=%s)", image, block_size)
    return image_array


def img_convolve(image, filter_kernel):
    logger.debug(">>> Entering img_convolve(image=%s,filter_kernel=%s)", image, filter_kernel)
    height, width = image.shape[0], image.shape[1]
    k_size = filter_kernel.shape[0]
    logger.debug("img_convolve(image=%s,filter_kernel=%s): k_size → %s", image, filter_kernel, k_size)
    pad_size = k_size // 2
    logger.debug("img_convolve(image=%s,filter_kernel=%s): pad_size → %s", image, filter_kernel, pad_size)
    # Pads image with the edge values of array.
    image_tmp = pad(image, pad_size, mode="edge")
    logger.debug("img_convolve(image=%s,filter_kernel=%s): image_tmp → %s", image, filter_kernel, image_tmp)

    # im2col, turn the k_size*k_size pixels into a row and np.vstack all rows
    image_array = im2col(image_tmp, (k_size, k_size))
    logger.debug("img_convolve(image=%s,filter_kernel=%s): image_array → %s", image, filter_kernel, image_array)

    #  turn the kernel into shape(k*k, 1)
    kernel_array = ravel(filter_kernel)
    logger.debug("img_convolve(image=%s,filter_kernel=%s): kernel_array → %s", image, filter_kernel, kernel_array)
    # reshape and get the dst image
    dst = dot(image_array, kernel_array).reshape(height, width)
    logger.debug("img_convolve(image=%s,filter_kernel=%s): dst → %s", image, filter_kernel, dst)
    logger.debug("<<< Exiting img_convolve(image=%s,filter_kernel=%s)", image, filter_kernel)
    return dst


if __name__ == "__main__":
    # read original image
    img = imread(r"../image_data/lena.jpg")
    # turn image in gray scale value
    gray = cvtColor(img, COLOR_BGR2GRAY)
    # Laplace operator
    Laplace_kernel = array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    out = img_convolve(gray, Laplace_kernel).astype(uint8)
    imshow("Laplacian", out)
    waitKey(0)
