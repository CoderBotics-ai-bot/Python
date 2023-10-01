#from computer_vision.mosaic_augmentation import *
#import pytest
#from typing import List, Tuple, Union
#import numpy as np
#
#import cv2
#
#
#import os
#
#
#def test_update_image_and_anno() -> None:
#    """
#    Test the update_image_and_anno function for proper execution and output type
#    """
#
#    # Sample data
#    all_img_list = ["test1.jpg", "test2.jpg"]
#    all_annos = [
#        [[0, 0.1, 0.2, 0.3, 0.4], [1, 0.5, 0.6, 0.7, 0.8]],
#        [[2, 0.1, 0.2, 0.3, 0.4], [3, 0.5, 0.6, 0.7, 0.8]],
#    ]
#    idxs = [0, 1]
#    output_size = (500, 500)
#    scale_range = (0.2, 0.8)
#    filter_scale = 0.02
#
#    # Generating sample images
#    img = np.zeros((500, 500, 3), np.uint8)
#    cv2.imwrite(all_img_list[0], img)
#    cv2.imwrite(all_img_list[1], img)
#
#    result = update_image_and_anno(
#        all_img_list, all_annos, idxs, output_size, scale_range, filter_scale
#    )
#
#    # Check that function executes successfully and returns not None
#    assert result is not None
#
#    # Check datatype of output
#    assert isinstance(result, tuple)
#    assert isinstance(result[0], np.ndarray)  # output_img should be an ndarray
#    assert isinstance(result[1], list)  # new_anno should be a list
#    assert isinstance(result[2], str)  # path_list[0] should be a string
#
#    # Clean up sample images
#    os.remove(all_img_list[0])
#    os.remove(all_img_list[1])
#