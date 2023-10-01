from computer_vision.flip_augmentation import *
import pytest


def test_update_image_and_anno_no_errors():
    img_list = ["test_img1.jpg", "test_img2.jpg", "test_img3.jpg"]
    anno_list = [
        [[1, 0.5, 0.5, 0.1, 0.1], [2, 0.6, 0.6, 0.2, 0.08]],
        [[3, 0.7, 0.7, 0.3, 0.05]],
        [[4, 0.8, 0.8, 0.4, 0.05]],
    ]
    flip_type = 1

    result = update_image_and_anno(img_list, anno_list, flip_type)
    assert result is not None


def test_update_image_and_anno_empty_input():
    img_list = []
    anno_list = []
    flip_type = 1

    result = update_image_and_anno(img_list, anno_list, flip_type)
    assert result[0] == []
    assert result[1] == []
    assert result[2] == []


def test_update_image_and_anno_flip_types():
    img_list = ["test_img1.jpg"]
    anno_list = [[[1, 0.5, 0.5, 0.1, 0.1]]]
    flip_type = 0

    result = update_image_and_anno(img_list, anno_list, flip_type)
    assert result[1][0][0][2] == 0.5

    flip_type = 1
    result = update_image_and_anno(img_list, anno_list, flip_type)
    assert result[1][0][0][1] == 0.5
