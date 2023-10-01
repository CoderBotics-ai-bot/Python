from computer_vision.flip_augmentation import update_image_and_anno

import cv2
import os
import numpy as np
import pytest


import pytest
from computer_vision.flip_augmentation import *


@pytest.fixture
def image_paths(tmp_path):
    base_path = tmp_path / "images"
    base_path.mkdir()
    img_paths = []
    for i in range(3):
        img = np.random.randint(0, 255, (50, 50, 3), dtype=np.uint8)

        img_path = base_path / f"image{i}.jpg"
        if not img_path.exists():
            cv2.imwrite(str(img_path), img)
        img_paths.append(str(img_path))
    return img_paths


def test_update_image_and_anno_no_errors(image_paths):
    anno_list = [[list(np.random.rand(5)) for _ in range(5)] for _ in range(5)]
    result = update_image_and_anno(image_paths, anno_list)
    assert result is not None


def test_update_image_and_anno_flip_types(image_paths):
    bbox = list(np.random.rand(5))
    result_horizontal = update_image_and_anno([image_paths[0]], [[bbox]], flip_type=1)
    result_vertical = update_image_and_anno([image_paths[0]], [[bbox]], flip_type=0)

    img = cv2.imread(image_paths[0])
    flipped_img_horizontal = cv2.flip(img, 1)
    flipped_img_vertical = cv2.flip(img, 0)

    assert np.array_equal(result_horizontal[0][0], flipped_img_horizontal)
    assert np.array_equal(result_vertical[0][0], flipped_img_vertical)


def test_update_image_and_anno_no_images():
    result = update_image_and_anno([], [])
    assert result == ([], [], [])


def test_update_image_and_anno_image_annotation_mismatch(image_paths):
    anno_list = [[list(np.random.rand(5)) for _ in range(4)]] + [
        [list(np.random.rand(5)) for _ in range(5)] for _ in range(2)
    ]
    result = update_image_and_anno(image_paths, anno_list)
    assert result is not None
