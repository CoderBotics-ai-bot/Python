#from PIL import Image
#from computer_vision.mean_threshold import *
#import numpy as np
#import pytest
#
#
#@pytest.fixture
#def create_image():
#    # Create a 5x5 grayscale image for testing
#    data = np.arange(25).reshape((5, 5)).astype(np.uint8)
#    img = Image.fromarray(data, "L")
#    return img
#
#
#def test_mean_threshold_no_error(create_image):
#    # Test that the function executes without errors
#    result = mean_threshold(create_image)
#    assert result is not None
#    assert isinstance(result, Image.Image)
#
#
#def test_mean_threshold_result(create_image):
#    # Test the result of the function
#    np_image = np.array(create_image)
#    mean = np_image.mean()
#    expected_result = np_image > mean
#    result = mean_threshold(create_image)
#    np_result = np.array(result)
#    np.testing.assert_array_equal(np_result, expected_result)
#
#
## Import necessary modules for testcase
#from typing import Tuple
#
#
## Need to define a fixture for small image size (1x1, 2x2)
#@pytest.fixture(params=[(1, 1), (2, 2)])
#def small_image(request: Tuple[int, int]) -> Image:
#    size = request.param
#    data = np.zeros(size, dtype=np.uint8)
#    return Image.fromarray(data, "L")
#
#
#def test_mean_threshold_small_image(small_image):
#    # Edge case to test a very small image (1x1 or 2x2)
#    result = mean_threshold(small_image)
#    assert result is not None
#    assert isinstance(result, Image.Image)
#