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
        logger.error(">>> Entering __init__(k=%s,window_size=%s)", k, window_size, extra={"event.action": "__init__", "logrite.k": k, "logrite.window_size": window_size})

        if k in (0.04, 0.06):
            self.k = k
            logger.debug("__init__(self=%s,k=%s,window_size=%s): self.k → %s", self, k, window_size, self.k, extra={"event.action": "__init__", "logrite.k": k, "logrite.window_size": window_size})
            self.window_size = window_size
        else:
            logger.debug("__init__(self=%s,k=%s,window_size=%s): self.window_size → %s", self, k, window_size, self.window_size, extra={"event.action": "__init__", "logrite.k": k, "logrite.window_size": window_size})
            logger.warning("<<< Exiting __init__(k=%s,window_size=%s)", k, window_size, extra={"event.action": "__init__", "logrite.k": k, "logrite.window_size": window_size})
            raise ValueError("invalid k value")

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return str(self.k)

    def detect(self, img_path: str) -> tuple[cv2.Mat, list[list[int]]]:
        """
        Returns the image with corners identified
        img_path  : path of the image
        output : list of the corner positions, image
        """
        logger.error(">>> Entering detect(img_path=%s)", img_path, extra={"event.action": "detect", "logrite.img_path": img_path})

        img = cv2.imread(img_path, 0)
        logger.error("detect(img_path=%s): img → %s", img_path, img, extra={"event.action": "detect", "logrite.img_path": img_path})
        h, w = img.shape
        corner_list: list[list[int]] = []
        color_img = img.copy()
        color_img = cv2.cvtColor(color_img, cv2.COLOR_GRAY2RGB)
        logger.error("detect(img_path=%s): color_img → %s", img_path, color_img, extra={"event.action": "detect", "logrite.img_path": img_path})
        dy, dx = np.gradient(img)
        ixx = dx**2
        iyy = dy**2
        ixy = dx * dy
        k = 0.04
        offset = self.window_size // 2
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
                logger.error("detect(img_path=%s): det → %s", img_path, det, extra={"event.action": "detect", "logrite.img_path": img_path})
                trace = wxx + wyy
                r = det - k * (trace**2)
                logger.error("detect(img_path=%s): r → %s", img_path, r, extra={"event.action": "detect", "logrite.img_path": img_path})
                # Can change the value
                if r > 0.5:
                    corner_list.append([x, y, r])
                    color_img.itemset((y, x, 0), 0)
                    color_img.itemset((y, x, 1), 0)
                    color_img.itemset((y, x, 2), 255)
        logger.warning("<<< Exiting detect(img_path=%s)", img_path, extra={"event.action": "detect", "logrite.img_path": img_path})
        return color_img, corner_list


if __name__ == "__main__":
    edge_detect = HarrisCorner(0.04, 3)
    color_img, _ = edge_detect.detect("path_to_image")
    cv2.imwrite("detect.png", color_img)
