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
    assert number_char > 1, "The number of character should greater than 1"
    letter_code = ascii_lowercase + digits
    return "".join(random.choice(letter_code) for _ in range(number_char))


if __name__ == "__main__":
    main()
    print("DONE ✅")
