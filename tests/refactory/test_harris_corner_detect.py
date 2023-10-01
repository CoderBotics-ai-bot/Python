#from computer_vision.harris_corner import *
#
#import cv2
#import numpy as np
#import pytest
#from typing import List
#
#
## Define a test case for the detect function
#def test_detect():
#    from my_module import HarrisCorner
#
#    # Creating a synthetic image
#    img = np.zeros((5, 5, 3))
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    cv2.imwrite("img.jpg", img)
#    # Creating an instance of the class
#    harris = HarrisCorner(k=0.04, window_size=2)
#    # Testing detect method
#    result_img, result_corner_list = harris.detect("img.jpg")
#    assert result_img is not None
#    assert result_corner_list is not None
#
#
## Define a test case for checking ValueError for invalid 'k' in HarrisCorner initialization
#def test_invalid_k_value():
#    from my_module import HarrisCorner
#
#    with pytest.raises(ValueError):
#        HarrisCorner(k=0.03, window_size=5)  # k not in [0.04,0.06]
#
#
## Define a test case checking Attribute Error for accessing an invalid attribute
#def test_invalid_attribute():
#    from my_module import HarrisCorner
#
#    harris = HarrisCorner(k=0.04, window_size=2)
#    with pytest.raises(AttributeError):
#        print(harris.invalid_attribute)  # Accessing an invalid attribute
#