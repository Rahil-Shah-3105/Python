import cv2
import numpy as np
import logging
logger = logging.getLogger(__name__)

"""
Harris Corner Detector
https://en.wikipedia.org/wiki/Harris_Corner_Detector
"""


class HarrisCorner:
    def __init__(self, k: float, window_size: int):
        """
        k : is an empirically determined constant in [0.04,0.06]
        window_size : neighbourhoods considered
        """
        logger.debug(">>> Entering __init__(k=%s,window_size=%s)", k, window_size)

        if k in (0.04, 0.06):
            self.k = k
            logger.debug("__init__(self=%s,k=%s,window_size=%s): self.k → %s", self, k, window_size, self.k)
            self.window_size = window_size
            logger.debug("__init__(self=%s,k=%s,window_size=%s): self.window_size → %s", self, k, window_size, self.window_size)
        else:
            logger.debug("<<< Exiting __init__(k=%s,window_size=%s)", k, window_size)
            raise ValueError("invalid k value")

    def __str__(self) -> str:
        logger.debug(">>> Entering __str__()")
        logger.debug("<<< Exiting __str__()")
        return str(self.k)

    def detect(self, img_path: str) -> tuple[cv2.Mat, list[list[int]]]:
        """
        Returns the image with corners identified
        img_path  : path of the image
        output : list of the corner positions, image
        """
        logger.debug(">>> Entering detect(img_path=%s)", img_path)
        logger.debug("detect(img_path=%s): color_img → %s", img_path, color_img)

        img = cv2.imread(img_path, 0)
        logger.debug("detect(self=%s,img_path=%s): img → %s", self, img_path, img)
        logger.debug("detect(img_path=%s): img → %s", img_path, img)
        h, w = img.shape
        corner_list: list[list[int]] = []
        color_img = img.copy()
        color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2RGB)
        logger.debug("detect(self=%s,img_path=%s): color_img → %s", self, img_path, color_img)
        dy, dx = np.gradient(img)
        ixx = dx**2
        logger.debug("detect(self=%s,img_path=%s): ixx → %s", self, img_path, ixx)
        iyy = dy**2
        logger.debug("detect(self=%s,img_path=%s): iyy → %s", self, img_path, iyy)
        ixy = dx * dy
        logger.debug("detect(self=%s,img_path=%s): ixy → %s", self, img_path, ixy)
        k = 0.04
        offset = self.window_size // 2
        logger.debug("detect(self=%s,img_path=%s): offset → %s", self, img_path, offset)
        for y in range(offset, h - offset):
            for x in range(offset, w - offset):
                wxx = ixx[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()
                wyy = iyy[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()
                wxy = ixy[
                    y - offset : y + offset + 1, x - offset : x + offset + 1
                ].sum()

                det = (wxx * wyy) - (wxy**2)
                logger.debug("detect(self=%s,img_path=%s): det → %s", self, img_path, det)
                logger.debug("detect(img_path=%s): det → %s", img_path, det)
                trace = wxx + wyy
                logger.debug("detect(self=%s,img_path=%s): trace → %s", self, img_path, trace)
                r = det - k * (trace**2)
                logger.debug("detect(img_path=%s): r → %s", img_path, r)
                # Can change the value
                if r > 0.5:
                    corner_list.append([x, y, r])
                    color_img.itemset((y, x, 0), 0)
                    color_img.itemset((y, x, 1), 0)
                    color_img.itemset((y, x, 2), 255)
        logger.debug("<<< Exiting detect(img_path=%s)", img_path)
        return color_img, corner_list


if __name__ == "__main__":
    edge_detect = HarrisCorner(0.04, 3)
    color_img, _ = edge_detect.detect("path_to_image")
    cv2.imwrite("detect.png", color_img)
