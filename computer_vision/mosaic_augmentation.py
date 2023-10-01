"""Source: https://github.com/jason9075/opencv-mosaic-data-aug"""

import glob
import os
import random
from string import ascii_lowercase, digits

import cv2
import numpy as np


from typing import None


from typing import List


from typing import List, Union, Tuple


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
    all_img_list: List[str],
    all_annos: List[List[List[Union[int, float]]]],
    idxs: List[int],
    output_size: Tuple[int, int],
    scale_range: Tuple[float, float],
    filter_scale: float = 0.0,
) -> Tuple[np.ndarray, List[List[Union[int, float]]], str]:
    """
    Updates the image and its corresponding annotations based on scaling.
    Parameters:
        all_img_list: List of all image file paths.
        all_annos: List of lists of annotations corresponding to each image.
        idxs: List of indices of images from `all_img_list` to be considered.
        output_size: Tuple specifying the desired output size (Height, Width).
        scale_range: Tuple specifying the scaling range.
        filter_scale: Minimum filter scale. Default value is 0.0.
    Returns:
        A tuple containing the updated image array, new annotations, and the file path of the first image.
    """

    def _update_quadrant(
        scale_x: float,
        scale_y: float,
        img: np.ndarray,
        img_annos: List[List[Union[int, float]]],
        i: int,
    ) -> Tuple[np.ndarray, List[List[Union[int, float]]]]:
        coords_bounds = [
            (scale_x, scale_y),
            (1 - scale_x, scale_y),
            (scale_x, 1 - scale_y),
            (1 - scale_x, 1 - scale_y),
        ]
        x_mul, y_mul = coords_bounds[i]
        new_size = (int(x_mul * output_size[1]), int(y_mul * output_size[0]))
        img = cv2.resize(img, new_size)
        new_annos = [
            [
                bbox[0],
                bbox[1] * x_mul,
                bbox[2] * y_mul,
                bbox[3] * x_mul,
                bbox[4] * y_mul,
            ]
            for bbox in img_annos
        ]
        return img, new_annos

    output_img = np.zeros([output_size[0], output_size[1], 3], dtype=np.uint8)
    scale_x = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    scale_y = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    divid_point_x = int(scale_x * output_size[1])
    divid_point_y = int(scale_y * output_size[0])

    scale_bounds = [
        (0, divid_point_y, 0, divid_point_x),
        (0, divid_point_y, divid_point_x, output_size[1]),
        (divid_point_y, output_size[0], 0, divid_point_x),
        (divid_point_y, output_size[0], divid_point_x, output_size[1]),
    ]
    new_anno = []
    path_list = []
    for i, index in enumerate(idxs):
        path = all_img_list[index]
        path_list.append(path)
        img = cv2.imread(path)
        img, img_annos = _update_quadrant(scale_x, scale_y, img, all_annos[index], i)
        y1, y2, x1, x2 = scale_bounds[i]
        output_img[y1:y2, x1:x2, :] = img
        new_anno.extend(img_annos)

    new_anno = [
        anno
        for anno in new_anno
        if filter_scale < (anno[3] - anno[1]) and filter_scale < (anno[4] - anno[2])
    ]
    return output_img, new_anno, path_list[0]


def main() -> None:
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
        print(f"Succeeded {index+1}/{NUMBER_IMAGES}")
        annos_list = generate_annos_list(new_annos)
        save_annos(file_root, annos_list)


def get_dataset(
    label_dir: str, img_dir: str
) -> Tuple[List[str], List[List[List[Union[int, float]]]]]:
    img_paths = []
    labels = []
    for label_file in glob.glob(os.path.join(label_dir, "*.txt")):
        label_name = os.path.basename(label_file).rsplit(".", 1)[0]
        img_path = os.path.join(img_dir, f"{label_name}.jpg")

        obj_lists = getParsedObjects(label_file)
        boxes = getBoundingBoxes(obj_lists)

        if not boxes:
            continue
        img_paths.append(img_path)
        labels.append(boxes)
    return img_paths, labels

def generate_file_root(output_dir: str, path: str, letter_code: str) -> str:
    file_name = path.split(os.sep)[-1].rsplit(".", 1)[0]
    return f"{output_dir}/{file_name}_MOSAIC_{letter_code}"

def getParsedObjects(label_file: str) -> List[str]:
    """Reads and parses object lists from a given label file.

    Args:
        label_file (str): The path to the label file.

    Returns:
        List[str]: A list of parsed objects.
    """
    with open(label_file) as in_file:
        obj_lists = in_file.readlines()
    return obj_lists


def getBoundingBoxes(obj_lists: List[str]) -> List[List[Union[int, float]]]:
    """Calculates bounding boxes coordinates for given list of parsed objects.

    Args:
        obj_lists (List[str]): A list of parsed objects.

    Returns:
        List[List[Union[int, float]]]: A list of bounding boxes.
            Each bounding box is a list where first element is an object id
            and rest elements represent bounding box coordinates.
    """
    boxes = []
    for obj_list in obj_lists:
        obj = obj_list.rstrip("\n").split(" ")
        xmin = float(obj[1]) - float(obj[3]) / 2
        ymin = float(obj[2]) - float(obj[4]) / 2
        xmax = float(obj[1]) + float(obj[3]) / 2
        ymax = float(obj[2]) + float(obj[4]) / 2

        boxes.append([int(obj[0]), xmin, ymin, xmax, ymax])
    return boxes


def save_image(file_root: str, new_image) -> None:
    cv2.imwrite(f"{file_root}.jpg", new_image, [cv2.IMWRITE_JPEG_QUALITY, 85])


def generate_annos_list(new_annos) -> list:
    annos_list = []
    for anno in new_annos:
        width = anno[3] - anno[1]
        height = anno[4] - anno[2]
        x_center = anno[1] + width / 2
        y_center = anno[2] + height / 2
        obj = f"{anno[0]} {x_center} {y_center} {width} {height}"
        annos_list.append(obj)
    return annos_list


def save_annos(file_root: str, annos_list: list) -> None:
    with open(f"{file_root}.txt", "w") as outfile:
        outfile.write("\n".join(line for line in annos_list))


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


if __name__ == "__main__":
    main()
    print("DONE ✅")
