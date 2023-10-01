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


def update_image_and_anno(
    all_img_list, all_annos, idxs, output_size, scale_range, filter_scale=0.0
):
    output_img = np.zeros([output_size[0], output_size[1], 3], dtype=np.uint8)
    scale_x = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    scale_y = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])

    new_anno = []
    path_list = []

    scale_dimensions = [
        (scale_x, scale_y),
        (1 - scale_x, scale_y),
        (scale_x, 1 - scale_y),
        (1 - scale_x, 1 - scale_y),
    ]
    output_img_coords = [
        (0, 0),
        (int(scale_x * output_size[1]), 0),
        (0, int(scale_y * output_size[0])),
        (int(scale_x * output_size[1]), int(scale_y * output_size[0])),
    ]

    for i, index in enumerate(idxs):
        img_annos = all_annos[index]
        img = cv2.imread(all_img_list[index])
        resized_img, annos = _update_image_and_anno_segment(
            img, img_annos, scale_dimensions[i], output_size, output_img_coords[i]
        )
        new_anno += annos
        output_img[
            output_img_coords[i][1] : output_img_coords[i][1] + resized_img.shape[0],
            output_img_coords[i][0] : output_img_coords[i][0] + resized_img.shape[1],
            :,
        ] = resized_img
        path_list.append(all_img_list[index])

    if filter_scale > 0.0:
        new_anno = _filter_annotations(new_anno, filter_scale)

    return output_img, new_anno, path_list[0]


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

def _get_scaled_dimensions(scale, output_size):
    return int(scale[0] * output_size[0]), int(scale[1] * output_size[1])


def _update_anno_for_segment(annotations, scale, additional_scale):
    return [
        [
            bbox[0],
            scale[0] + bbox[1] * additional_scale[0],
            scale[1] + bbox[2] * additional_scale[1],
            scale[0] + bbox[3] * additional_scale[0],
            scale[1] + bbox[4] * additional_scale[1],
        ]
        for bbox in annotations
    ]


def _update_image_and_anno_segment(
    image, annotations, scale, output_img_dims, output_img_coords
):
    scale_dimensions = _get_scaled_dimensions(scale, output_img_dims)
    dim = min(output_img_dims[0] - output_img_coords[0], scale_dimensions[0]), min(
        output_img_dims[1] - output_img_coords[1], scale_dimensions[1]
    )
    resized_img = cv2.resize(image, dim)
    new_annotations = _update_anno_for_segment(
        annotations, scale, (1 - scale[0], 1 - scale[1])
    )
    return resized_img, new_annotations


def _filter_annotations(annotations, filter_scale):
    return [
        anno
        for anno in annotations
        if filter_scale < (anno[3] - anno[1]) and filter_scale < (anno[4] - anno[2])
    ]

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
