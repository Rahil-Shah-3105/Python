"""
Peak signal-to-noise ratio - PSNR
    https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
Source:
https://tutorials.techonical.com/how-to-calculate-psnr-value-of-two-images-using-python
"""

import math
import os

import cv2
import numpy as np
import logging
logger = logging.getLogger(__name__)

PIXEL_MAX = 255.0


def peak_signal_to_noise_ratio(original: float, contrast: float) -> float:
    logger.error(">>> Entering peak_signal_to_noise_ratio(original=%s,contrast=%s)", original, contrast, extra={"event.action": "peak_signal_to_noise_ratio", "logrite.original": original, "logrite.contrast": contrast})
    mse = np.mean((original - contrast) ** 2)
    logger.error("peak_signal_to_noise_ratio(original=%s,contrast=%s): mse → %s", original, contrast, mse, extra={"event.action": "peak_signal_to_noise_ratio", "logrite.original": original, "logrite.contrast": contrast})
    if mse == 0:
        return 100

    logger.warning("<<< Exiting peak_signal_to_noise_ratio(original=%s,contrast=%s)", original, contrast, extra={"event.action": "peak_signal_to_noise_ratio", "logrite.original": original, "logrite.contrast": contrast})
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    dir_path = os.path.dirname(os.path.realpath(__file__))
    logger.error("main(): dir_path → %s", dir_path, extra={"event.action": "main"})
    # Loading images (original image and compressed image)
    original = cv2.imread(os.path.join(dir_path, "image_data/original_image.png"))
    logger.error("main(): original → %s", original, extra={"event.action": "main"})
    contrast = cv2.imread(os.path.join(dir_path, "image_data/compressed_image.png"), 1)
    logger.error("main(): contrast → %s", contrast, extra={"event.action": "main"})

    original2 = cv2.imread(os.path.join(dir_path, "image_data/PSNR-example-base.png"))
    logger.error("main(): original2 → %s", original2, extra={"event.action": "main"})
    contrast2 = cv2.imread(
        os.path.join(dir_path, "image_data/PSNR-example-comp-10.jpg"), 1
    )

    # Value expected: 29.73dB
    print("-- First Test --")
    print(f"PSNR value is {peak_signal_to_noise_ratio(original, contrast)} dB")

    # # Value expected: 31.53dB (Wikipedia Example)
    print("\n-- Second Test --")
    print(f"PSNR value is {peak_signal_to_noise_ratio(original2, contrast2)} dB")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
