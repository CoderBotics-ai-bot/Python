from computer_vision.mosaic_augmentation import *

import cv2
from random import sample
import numpy as np
import pytest
from typing import Dict, List, Tuple


# fixture to provide necessary sample data to test the function
@pytest.fixture
def sample_data():
    img_path1 = "test_img1.jpg"
    img_path2 = "test_img2.jpg"
    img_path3 = "test_img3.jpg"
    img_path4 = "test_img4.jpg"

    img1 = np.zeros((100, 100, 3), dtype=np.uint8)
    img2 = np.zeros((100, 100, 3), dtype=np.uint8)
    img3 = np.zeros((100, 100, 3), dtype=np.uint8)
    img4 = np.zeros((100, 100, 3), dtype=np.uint8)

    cv2.imwrite(img_path1, img1)
    cv2.imwrite(img_path2, img2)
    cv2.imwrite(img_path3, img3)
    cv2.imwrite(img_path4, img4)

    all_img_list = [img_path1, img_path2, img_path3, img_path4]
    all_annos = [
        [[0, 25, 25, 75, 75]],
        [[1, 25, 25, 75, 75]],
        [[2, 25, 25, 75, 75]],
        [[3, 25, 25, 75, 75]],
    ]
    idxs = sample(list(range(4)), k=4)
    output_size = (200, 200)
    scale_range = (0.5, 1.5)
    filter_scale = 0.0

    yield {
        "all_img_list": all_img_list,
        "all_annos": all_annos,
        "idxs": idxs,
        "output_size": output_size,
        "scale_range": scale_range,
        "filter_scale": filter_scale,
    }
    os.remove(img_path1)
    os.remove(img_path2)
    os.remove(img_path3)
    os.remove(img_path4)


def test_update_image_and_anno_execution(sample_data):
    output_img, new_anno, path = update_image_and_anno(
        sample_data["all_img_list"],
        sample_data["all_annos"],
        sample_data["idxs"],
        sample_data["output_size"],
        sample_data["scale_range"],
        sample_data["filter_scale"],
    )
    assert output_img is not None
    assert new_anno is not None
    assert path is not None


def test_update_image_and_anno_with_empty_img_list(sample_data):
    with pytest.raises(Exception):
        _, _, _ = update_image_and_anno(
            [],
            sample_data["all_annos"],
            sample_data["idxs"],
            sample_data["output_size"],
            sample_data["scale_range"],
            sample_data["filter_scale"],
        )


def test_update_image_and_anno_with_invalid_index(sample_data):
    with pytest.raises(Exception):
        _, _, _ = update_image_and_anno(
            sample_data["all_img_list"],
            sample_data["all_annos"],
            [10, 20, 30, 40],
            sample_data["output_size"],
            sample_data["scale_range"],
            sample_data["filter_scale"],
        )
