import glob
import os
import random
from string import ascii_lowercase, digits

import cv2


from pathlib import Path
from typing import List, Tuple


import numpy as np

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
    Get images and annotations from input directories. Modify the images by flipping
    horizontally or vertically based on the flip type. Store modified images and annotations
    in the output directory.

    The function doesn't return anything, but has a side-effect of creating new image and annotations files
    in the `OUTPUT_DIR` directory.

    The function doesn't take any arguments, it operates based on the global variables `LABEL_DIR`, `IMAGE_DIR`,
    `OUTPUT_DIR` and `FLIP_TYPE`.
    """
    img_paths, annos = get_dataset(LABEL_DIR, IMAGE_DIR)
    print("Processing...")
    new_images, new_annos, paths = update_image_and_anno(img_paths, annos, FLIP_TYPE)

    for index, image in enumerate(new_images):
        file_name = get_file_name(paths[index])
        file_root = f"{OUTPUT_DIR}/{file_name}_FLIP_{random_chars(32)}"
        save_image(image, file_root)
        print(f"Success {index+1}/{len(new_images)} with {file_name}")
        save_annotations(new_annos[index], file_root)


def get_file_name(path: str) -> str:
    return Path(path).stem


def update_image_and_anno(
    img_list: List[str], anno_list: List[List[float]], flip_type: int = 1
) -> Tuple[List[str], List[List[List[float]]], List[str]]:
    if flip_type not in {0, 1}:
        raise ValueError("flip_type must be either 0 or 1")

    new_annos_lists = []
    new_imgs_list = []
    path_list = img_list.copy()

    flip_axis_index = 1 if flip_type == 1 else 2

    for path, annotations in zip(path_list, anno_list):
        image = cv2.imread(path)
        new_image = flip_image(image, flip_type)
        new_annotations = update_annotations(annotations, flip_axis_index)

        new_annos_lists.append(new_annotations)
        new_imgs_list.append(new_image)

    return new_imgs_list, new_annos_lists, path_list

def get_dataset(
    label_dir: str, img_dir: str
) -> Tuple[List[str], List[List[List[float]]]]:
    img_paths, labels = [], []

    for label_file in sorted(glob.glob(f"{label_dir}/*.txt")):
        label_name = Path(label_file).stem
        boxes = parse_boxes_from_file(label_file)
        if not boxes:
            continue
        img_path = str(Path(img_dir) / f"{label_name}.jpg")
        img_paths.append(img_path)
        labels.append(boxes)

    return img_paths, labels

def flip_image(image: np.array, flip_type: int) -> np.array:
    """Flips the given image based on the type of flip."""
    return cv2.flip(image, flip_type)


def update_annotations(
    annotations: List[List[float]], flip_axis_index: int
) -> List[List[float]]:
    """Updates the annotations based on the axis of flip."""
    new_annotations = []
    for bbox in annotations:
        axis_value_new = 1 - bbox[flip_axis_index]
        new_bbox = bbox.copy()
        new_bbox[flip_axis_index] = axis_value_new
        new_annotations.append(new_bbox)

    return new_annotations


def save_image(image, file_root: str) -> None:
    cv2.imwrite(f"/{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 85])


def parse_boxes_from_file(file_path: str) -> List[List[float]]:
    with open(file_path) as in_file:
        obj_lists = in_file.readlines()

    return [parse_single_box(obj_list) for obj_list in obj_lists]


def parse_single_box(obj_list: str) -> List[float]:
    obj = obj_list.rstrip("\n").split(" ")
    return [int(obj[0])] + [float(x) for x in obj[1:]]


def save_annotations(annotations: list, file_root: str) -> None:
    annos_list = [
        f"{anno[0]} {anno[1]} {anno[2]} {anno[3]} {anno[4]}" for anno in annotations
    ]
    with open(f"/{file_root}.txt", "w") as outfile:
        outfile.write("\n".join(annos_list))


def random_chars(number_char: int = 32) -> str:
    """
    Automatic generate random 32 characters.
    Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
    >>> len(random_chars(32))
    32
    """
    assert number_char > 1, "The number of character should greater than 1"
    letter_code = ascii_lowercase + digits
    return "".join(random.choice(letter_code) for _ in range(number_char))


if __name__ == "__main__":
    main()
    print("DONE ✅")
