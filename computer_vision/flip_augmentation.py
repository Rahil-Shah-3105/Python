import glob
import os
import random
from string import ascii_lowercase, digits

import cv2
import logging
logger = logging.getLogger(__name__)

"""
Flip image and bounding box for computer vision task
https://paperswithcode.com/method/randomhorizontalflip
"""

# Params
LABEL_DIR = ""
IMAGE_DIR = ""
OUTPUT_DIR = ""
FLIP_TYPE = 1  # (0 is vertical, 1 is horizontal)


def main() -> None:
    """
    Get images list and annotations list from input dir.
    Update new images and annotations.
    Save images and annotations in output dir.
    """
    logger.debug(">>> Entering main()")
    img_paths, annos = get_dataset(LABEL_DIR, IMAGE_DIR)
    print("Processing...")
    new_images, new_annos, paths = update_image_and_anno(img_paths, annos, FLIP_TYPE)

    for index, image in enumerate(new_images):
        # Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
        letter_code = random_chars(32)
        logger.debug("main(): letter_code → %s", letter_code)
        file_name = paths[index].split(os.sep)[-1].rsplit(".", 1)[0]
        logger.debug("main(): file_name → %s", file_name)
        file_root = f"{OUTPUT_DIR}/{file_name}_FLIP_{letter_code}"
        logger.debug("main(): file_root → %s", file_root)
        cv2.imwrite(f"{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 85])
        print(f"Success {index + 1}/{len(new_images)} with {file_name}")
        annos_list = []
        logger.debug("main(): annos_list → %s", annos_list)
        for anno in new_annos[index]:
            obj = f"{anno[0]} {anno[1]} {anno[2]} {anno[3]} {anno[4]}"
            logger.debug("main(): obj → %s", obj)
            annos_list.append(obj)
        with open(f"{file_root}.txt", "w") as outfile:
            logger.error("Exception in main()", exc_info=True)
            outfile.write("\n".join(line for line in annos_list))
            logger.debug("<<< Exiting main()")


def get_dataset(label_dir: str, img_dir: str) -> tuple[list, list]:
    """
    - label_dir <type: str>: Path to label include annotation of images
    - img_dir <type: str>: Path to folder contain images
    Return <type: list>: List of images path and labels
    """
    logger.debug(">>> Entering get_dataset(label_dir=%s,img_dir=%s)", label_dir, img_dir)
    img_paths = []
    logger.debug("get_dataset(label_dir=%s,img_dir=%s): img_paths → %s", label_dir, img_dir, img_paths)
    labels = []
    logger.debug("get_dataset(label_dir=%s,img_dir=%s): labels → %s", label_dir, img_dir, labels)
    for label_file in glob.glob(os.path.join(label_dir, "*.txt")):
        label_name = label_file.split(os.sep)[-1].rsplit(".", 1)[0]
        logger.debug("get_dataset(label_dir=%s,img_dir=%s): label_name → %s", label_dir, img_dir, label_name)
        logger.debug("get_dataset(label_dir=%s,img_dir=%s): obj_lists → %s", label_dir, img_dir, obj_lists)
        logger.debug("get_dataset(label_dir=%s,img_dir=%s): img_path → %s", label_dir, img_dir, img_path)
        with open(label_file) as in_file:
            logger.error("Exception in get_dataset(label_dir=%s,img_dir=%s)", label_dir, img_dir, exc_info=True)
            obj_lists = in_file.readlines()
        img_path = os.path.join(img_dir, f"{label_name}.jpg")

        boxes = []
        logger.debug("get_dataset(label_dir=%s,img_dir=%s): boxes → %s", label_dir, img_dir, boxes)
        for obj_list in obj_lists:
            obj = obj_list.rstrip("\n").split(" ")
            logger.debug("get_dataset(label_dir=%s,img_dir=%s): obj → %s", label_dir, img_dir, obj)
            boxes.append(
                [
                    int(obj[0]),
                    float(obj[1]),
                    float(obj[2]),
                    float(obj[3]),
                    float(obj[4]),
                ]
            )
        if not boxes:
            continue
        img_paths.append(img_path)
        labels.append(boxes)
    logger.debug("<<< Exiting get_dataset(label_dir=%s,img_dir=%s)", label_dir, img_dir)
    return img_paths, labels


def update_image_and_anno(
    img_list: list, anno_list: list, flip_type: int = 1
) -> tuple[list, list, list]:
    """
    - img_list <type: list>: list of all images
    - anno_list <type: list>: list of all annotations of specific image
    - flip_type <type: int>: 0 is vertical, 1 is horizontal
    Return:
        - new_imgs_list <type: narray>: image after resize
        - new_annos_lists <type: list>: list of new annotation after scale
        - path_list <type: list>: list the name of image file
    """
    new_annos_lists = []
    path_list = []
    new_imgs_list = []
    for idx in range(len(img_list)):
        new_annos = []
        path = img_list[idx]
        path_list.append(path)
        img_annos = anno_list[idx]
        img = cv2.imread(path)
        if flip_type == 1:
            new_img = cv2.flip(img, flip_type)
            for bbox in img_annos:
                x_center_new = 1 - bbox[1]
                new_annos.append([bbox[0], x_center_new, bbox[2], bbox[3], bbox[4]])
        elif flip_type == 0:
            new_img = cv2.flip(img, flip_type)
            for bbox in img_annos:
                y_center_new = 1 - bbox[2]
                new_annos.append([bbox[0], bbox[1], y_center_new, bbox[3], bbox[4]])
        new_annos_lists.append(new_annos)
        new_imgs_list.append(new_img)
    return new_imgs_list, new_annos_lists, path_list


def random_chars(number_char: int = 32) -> str:
    """
    Automatic generate random 32 characters.
    Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
    >>> len(random_chars(32))
    32
    """
    logger.debug(">>> Entering random_chars(number_char=%s)", number_char)
    assert number_char > 1, "The number of character should greater than 1"
    letter_code = ascii_lowercase + digits
    logger.debug("random_chars(number_char=%s): letter_code → %s", number_char, letter_code)
    logger.debug("<<< Exiting random_chars(number_char=%s)", number_char)
    return "".join(random.choice(letter_code) for _ in range(number_char))


if __name__ == "__main__":
    main()
    print("DONE ✅")
