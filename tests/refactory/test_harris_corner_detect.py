import pytest
import numpy as np

import cv2
from computer_vision.harris_corner import *
from typing import Tuple


def test_harris_corner_detect_no_errors():
    """
    Test if HarrisCorner detect function doesn't throw errors when it's executed.
    """
    test_image = np.ones((5, 5), dtype=np.uint8) * 255
    cv2.imwrite("test_image.jpg", test_image)
    hc = HarrisCorner(k=0.04, window_size=5)
    output = hc.detect("test_image.jpg")
    assert output is not None


def test_harris_corner_detect_output_type():
    """
    Test if HarrisCorner detect function returns a tuple with nd.array and list.
    """
    test_image = np.ones((5, 5), dtype=np.uint8) * 255
    cv2.imwrite("test_image.jpg", test_image)
    hc = HarrisCorner(k=0.04, window_size=5)
    output = hc.detect("test_image.jpg")
    assert isinstance(output[0], np.ndarray)
    assert isinstance(output[1], list)


def test_harris_corner_init_invalid_k_value_throws_exception():
    """
    Test if a ValueError is raised when an invalid k value is passed to the constructor.
    """
    with pytest.raises(ValueError):
        HarrisCorner(k=0.03, window_size=5)
