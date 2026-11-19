"""
Created on Fri Sep 28 15:22:29 2018

@author: Binish125
"""

import copy
import os

import cv2
import numpy as np
from matplotlib import pyplot as plt
import logging
logger = logging.getLogger(__name__)


class ConstantStretch:
    def __init__(self):
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.img = ""
        logger.debug("__init__(self=%s): self.img → %s", self, self.img, extra={"event.action": "__init__"})
        logger.error("__init__(): self.img → %s", self.img, extra={"event.action": "__init__"})
        self.original_image = ""
        self.last_list = []
        logger.debug("__init__(self=%s): self.original_image → %s", self, self.original_image, extra={"event.action": "__init__"})
        logger.error("__init__(): self.original_image → %s", self.original_image, extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.last_list → %s", self, self.last_list, extra={"event.action": "__init__"})
        self.rem = 0
        self.L = 256
        self.sk = 0
        logger.debug("__init__(self=%s): self.rem → %s", self, self.rem, extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.L → %s", self, self.L, extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.sk → %s", self, self.sk, extra={"event.action": "__init__"})
        self.k = 0
        self.number_of_rows = 0
        logger.debug("__init__(self=%s): self.number_of_rows → %s", self, self.number_of_rows, extra={"event.action": "__init__"})
        self.number_of_cols = 0
        logger.debug("__init__(self=%s): self.k → %s", self, self.k, extra={"event.action": "__init__"})

    def stretch(self, input_image):
        logger.error(">>> Entering stretch(input_image=%s)", input_image, extra={"event.action": "stretch", "logrite.input_image": input_image})
        self.img = cv2.imread(input_image, 0)
        logger.error("stretch(input_image=%s): self.img → %s", input_image, self.img, extra={"event.action": "stretch", "logrite.input_image": input_image})
        self.original_image = copy.deepcopy(self.img)
        logger.error("stretch(input_image=%s): self.original_image → %s", input_image, self.original_image, extra={"event.action": "stretch", "logrite.input_image": input_image})
        x, _, _ = plt.hist(self.img.ravel(), 256, [0, 256], label="x")
        self.k = np.sum(x)
        for i in range(len(x)):
            prk = x[i] / self.k
            self.sk += prk
            last = (self.L - 1) * self.sk
            logger.error("stretch(input_image=%s): last → %s", input_image, last, extra={"event.action": "stretch", "logrite.input_image": input_image})
            if self.rem != 0:
                self.rem = int(last % last)
                logger.error("stretch(input_image=%s): self.rem → %s", input_image, self.rem, extra={"event.action": "stretch", "logrite.input_image": input_image})
            last = int(last + 1 if self.rem >= 0.5 else last)
            self.last_list.append(last)
            self.number_of_rows = int(np.ma.count(self.img) / self.img[1].size)
            logger.error("stretch(input_image=%s): self.number_of_rows → %s", input_image, self.number_of_rows, extra={"event.action": "stretch", "logrite.input_image": input_image})
            self.number_of_cols = self.img[1].size
            logger.debug("stretch(self=%s,input_image=%s): self.number_of_cols → %s", self, input_image, self.number_of_cols, extra={"event.action": "stretch", "logrite.input_image": input_image})
        for i in range(self.number_of_cols):
            for j in range(self.number_of_rows):
                num = self.img[j][i]
                if num != self.last_list[num]:
                    self.img[j][i] = self.last_list[num]
        cv2.imwrite("output_data/output.jpg", self.img)
        logger.warning("<<< Exiting stretch(input_image=%s)", input_image, extra={"event.action": "stretch", "logrite.input_image": input_image})

    def plot_histogram(self):
        logger.error(">>> Entering plot_histogram()", extra={"event.action": "plot_histogram"})
        plt.hist(self.img.ravel(), 256, [0, 256])
        logger.warning("<<< Exiting plot_histogram()", extra={"event.action": "plot_histogram"})

    def show_image(self):
        logger.error(">>> Entering show_image()", extra={"event.action": "show_image"})
        cv2.imshow("Output-Image", self.img)
        cv2.imshow("Input-Image", self.original_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
        logger.warning("<<< Exiting show_image()", extra={"event.action": "show_image"})


if __name__ == "__main__":
    file_path = os.path.join(os.path.basename(__file__), "image_data/input.jpg")
    stretcher = ConstantStretch()
    stretcher.stretch(file_path)
    stretcher.plot_histogram()
    stretcher.show_image()
