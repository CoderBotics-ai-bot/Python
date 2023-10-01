"""Source: https://github.com/jason9075/opencv-mosaic-data-aug"""

import glob
import os
import random
from string import ascii_lowercase, digits

import cv2
import numpy as np


from typing import List, Tuple, Union

# Parrameters
OUTPUT_SIZE = (720, 1280)  # Height, Width
SCALE_RANGE = (0.4, 0.6)  # if height or width lower than this scale, drop it.
FILTER_TINY_SCALE = 1 / 100
LABEL_DIR = ""
IMG_DIR = ""
OUTPUT_DIR = ""
NUMBER_IMAGES = 250


def update_image_and_anno(
    all_img_list: list,
    all_annos: list,
    idxs: list[int],
    output_size: tuple[int, int],
    scale_range: tuple[float, float],
    filter_scale: float = 0.0,
) -> tuple[list, list, str]:
    """
    - all_img_list <type: list>: list of all images
    - all_annos <type: list>: list of all annotations of specific image
    - idxs <type: list>: index of image in list
    - output_size <type: tuple>: size of output image (Height, Width)
    - scale_range <type: tuple>: range of scale image
    - filter_scale <type: float>: the condition of downscale image and bounding box
    Return:
        - output_img <type: narray>: image after resize
        - new_anno <type: list>: list of new annotation after scale
        - path[0] <type: string>: get the name of image file
    """
    output_img = np.zeros([output_size[0], output_size[1], 3], dtype=np.uint8)
    scale_x = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    scale_y = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    divid_point_x = int(scale_x * output_size[1])
    divid_point_y = int(scale_y * output_size[0])

    new_anno = []
    path_list = []
    for i, index in enumerate(idxs):
        path = all_img_list[index]
        path_list.append(path)
        img_annos = all_annos[index]
        img = cv2.imread(path)
        if i == 0:  # top-left
            img = cv2.resize(img, (divid_point_x, divid_point_y))
            output_img[:divid_point_y, :divid_point_x, :] = img
            for bbox in img_annos:
                xmin = bbox[1] * scale_x
                ymin = bbox[2] * scale_y
                xmax = bbox[3] * scale_x
                ymax = bbox[4] * scale_y
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
        elif i == 1:  # top-right
            img = cv2.resize(img, (output_size[1] - divid_point_x, divid_point_y))
            output_img[:divid_point_y, divid_point_x : output_size[1], :] = img
            for bbox in img_annos:
                xmin = scale_x + bbox[1] * (1 - scale_x)
                ymin = bbox[2] * scale_y
                xmax = scale_x + bbox[3] * (1 - scale_x)
                ymax = bbox[4] * scale_y
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
        elif i == 2:  # bottom-left
            img = cv2.resize(img, (divid_point_x, output_size[0] - divid_point_y))
            output_img[divid_point_y : output_size[0], :divid_point_x, :] = img
            for bbox in img_annos:
                xmin = bbox[1] * scale_x
                ymin = scale_y + bbox[2] * (1 - scale_y)
                xmax = bbox[3] * scale_x
                ymax = scale_y + bbox[4] * (1 - scale_y)
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
        else:  # bottom-right
            img = cv2.resize(
                img, (output_size[1] - divid_point_x, output_size[0] - divid_point_y)
            )
            output_img[
                divid_point_y : output_size[0], divid_point_x : output_size[1], :
            ] = img
            for bbox in img_annos:
                xmin = scale_x + bbox[1] * (1 - scale_x)
                ymin = scale_y + bbox[2] * (1 - scale_y)
                xmax = scale_x + bbox[3] * (1 - scale_x)
                ymax = scale_y + bbox[4] * (1 - scale_y)
                new_anno.append([bbox[0], xmin, ymin, xmax, ymax])

    # Remove bounding box small than scale of filter
    if filter_scale > 0:
        new_anno = [
            anno
            for anno in new_anno
            if filter_scale < (anno[3] - anno[1]) and filter_scale < (anno[4] - anno[2])
        ]

    return output_img, new_anno, path_list[0]


def main() -> None:
    """
    Get images list and annotations list from input dir.
    Update new images and annotations.
    Save images and annotations in output dir.
    """
    img_paths, annos = get_dataset(LABEL_DIR, IMG_DIR)
    for index in range(NUMBER_IMAGES):
        idxs = random.sample(range(len(annos)), 4)
        new_image, new_annos, path = update_image_and_anno(
            img_paths,
            annos,
            idxs,
            OUTPUT_SIZE,
            SCALE_RANGE,
            filter_scale=FILTER_TINY_SCALE,
        )

        letter_code = random_chars(32)
        file_root = generate_file_root(OUTPUT_DIR, path, letter_code)

        save_image(file_root, new_image)

        file_name = path.split(os.sep)[-1].rsplit(".", 1)[0]
        print_success(index, file_name)

        annos_list = [generate_anno_obj(anno) for anno in new_annos]
        save_annos(file_root, annos_list)


def get_dataset(
    label_dir: str, img_dir: str
) -> Tuple[List[str], List[List[Union[int, float]]]]:
    img_paths = []
    labels = []

    for label_file in glob.glob(os.path.join(label_dir, "*.txt")):
        img_path = get_dataset_path(label_dir, img_dir, label_file)
        boxes = get_boxes_from_label_file(label_file)

        if boxes:
            img_paths.append(img_path)
            labels.append(boxes)

    return img_paths, labels


def random_chars(number_char: int) -> str:
    """
    Automatic generate random 32 characters.
    Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
    >>> len(random_chars(32))
    32
    """
    assert number_char > 1, "The number of character should greater than 1"
    letter_code = ascii_lowercase + digits
    return "".join(random.choice(letter_code) for _ in range(number_char))

def get_dataset_path(label_dir: str, img_dir: str, label_file: str) -> str:
    """Computes the corresponding image file path from a label file path."""
    label_name = os.path.splitext(os.path.basename(label_file))[0]
    return os.path.join(img_dir, f"{label_name}.jpg")


def get_object_box(obj: List[str]) -> List[Union[int, float]]:
    """Helper function to compute bounding box coordinates."""
    xmin = float(obj[1]) - float(obj[3]) / 2
    ymin = float(obj[2]) - float(obj[4]) / 2
    xmax = float(obj[1]) + float(obj[3]) / 2
    ymax = float(obj[2]) + float(obj[4]) / 2

    return [int(obj[0]), xmin, ymin, xmax, ymax]


def get_boxes_from_label_file(label_file: str) -> List[List[Union[int, float]]]:
    """Reads a label file and returns all object boxes described within."""
    with open(label_file, "r") as file:
        box_lines = file.readlines()

    return [get_object_box(line.rstrip("\n").split(" ")) for line in box_lines]

def generate_anno_obj(anno: list) -> str:
    """
    Generate annotation object as a string
    """
    width = anno[3] - anno[1]
    height = anno[4] - anno[2]
    x_center = anno[1] + width / 2
    y_center = anno[2] + height / 2
    return f"{anno[0]} {x_center} {y_center} {width} {height}"


def print_success(index: int, file_name: str, total: int = NUMBER_IMAGES) -> None:
    """
    Print success message
    """
    print(f"Succeeded {index+1}/{total} with {file_name}")


if __name__ == "__main__":
    main()
    print("DONE ✅")
