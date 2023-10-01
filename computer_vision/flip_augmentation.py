import glob
import os
import random
from string import ascii_lowercase, digits

import cv2


from pathlib import Path


from typing import List, Tuple

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

def get_dataset(
    label_dir: str, img_dir: str
) -> Tuple[List[str], List[List[List[float]]]]:
    """
    Get the dataset from the provided folders.

    Args:
    label_dir(str): Folder path containing label files.
    img_dir(str): Folder path containing image files.

    Returns:
    Tuple[List[str], List[List[List[float]]]]: Tuple containing list of image paths and corresponding bounding boxes.
    """
    img_paths = []
    labels = []
    label_files = glob.glob(
        f"{label_dir}/*.txt"
    )  # Generate the correct glob pattern before use.

    for label_file in label_files:
        label_name = Path(label_file).stem
        obj_lists = get_content_in_file(label_file)
        boxes = get_boxes(obj_lists)

        if not boxes:
            continue

        img_path = get_image_path(img_dir, label_name)
        img_paths.append(img_path)
        labels.append(boxes)

    return img_paths, labels


def update_image_and_anno(
    img_list: List[str], anno_list: List[List[List[float]]], flip_type: int = 1
) -> Tuple[List, List[List[List[float]]], List[str]]:
    """
    Updates images and annotations by flipping the images and its annotations along
    a specified axis.

    Args:
        img_list: A list of file paths to the images.
        anno_list: A nested list of bounding box annotations for each image.
        flip_type: The type of flip to apply. Defaults to 1: horizontal flip.

    Returns:
        Tuple containing:
        - List of updated images after flip.
        - A nested list of updated annotations for each flipped image.
        - List of file paths to the images.
    """
    new_images = []
    new_annos = []

    for img, annos in zip(img_list, anno_list):
        new_img = cv2.flip(cv2.imread(img), flip_type)
        new_images.append(new_img)
        new_annos.append(update_annotations(annos, flip_type))

    return new_images, new_annos, img_list


def save_image(image, file_root: str) -> None:
    cv2.imwrite(f"/{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 85])

def update_annotations(
    annotations: List[List[float]], flip_type: int
) -> List[List[float]]:
    """
    Update the annotations for the flipped image.

    Args:
        annotations: A list of bounding box annotations for the image.
        flip_type: The type of flip applied to the image.

    Returns:
        A list of updated annotations for the flipped image.
    """

    if flip_type == 1:
        # Flip horizontally requires updating x_center
        return [
            [bbox[0], 1 - bbox[1], bbox[2], bbox[3], bbox[4]] for bbox in annotations
        ]

    # Flip vertically requires updating y_center
    return [[bbox[0], bbox[1], 1 - bbox[2], bbox[3], bbox[4]] for bbox in annotations]


def get_image_path(img_dir: str, label_name: str) -> str:
    return str(Path(img_dir) / f"{label_name}.jpg")


def get_content_in_file(label_file: str) -> List[str]:
    with open(label_file, "r") as in_file:
        lines = in_file.readlines()
    return lines


def get_boxes(obj_lists: List[str]) -> List[List[float]]:
    return [
        [int(obj[0]), float(obj[1]), float(obj[2]), float(obj[3]), float(obj[4])]
        for obj_list in obj_lists
        for obj in [obj_list.rstrip("\n").split()]
    ]


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
