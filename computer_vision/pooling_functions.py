# Source : https://computersciencewiki.org/index.php/Max-pooling_/_Pooling
# Importing the libraries
import numpy as np
from PIL import Image


import numpy as np


from typing import Tuple

def maxpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    Perform a maxpooling operation on a 2D numpy array (image) with the specified
    size and stride. The operation will extract the max element from non-overlapping
    submatrices (pools) of the input array.

    Args:
        arr (np.ndarray): The 2D input array to perform the maxpooling operation on.
            Expected to be a square matrix.
        size (int): The size of the pooling matrix, which will slide over the
            input array.
        stride (int): The number of pixels shifts over the input matrix when
            performing the pooling operation.

    Returns:
        np.ndarray: A new 2D numpy array of maxpooled matrix.

    Raises:
        ValueError: If the input array is not a square matrix.
    """
    arr = np.array(arr)
    validate_input(arr, size, stride)
    output_shape = compute_output_shape(arr, size, stride)
    updated_arr = np.zeros(output_shape)

    for i in range(0, output_shape[0]):
        for j in range(0, output_shape[1]):
            updated_arr[i][j] = np.max(
                arr[i * stride : i * stride + size, j * stride : j * stride + size]
            )

    return updated_arr


# Averagepooling Function
def avgpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    This function is used to perform avgpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of avgpooled matrix
    Sample Input Output:
    >>> avgpooling([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 3.,  5.],
           [11., 13.]])
    >>> avgpooling([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[161., 102.],
           [114.,  69.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0

    # compute the shape of the output matrix
    avgpool_shape = (arr.shape[0] - size) // stride + 1
    # initialize the output matrix with zeros of shape avgpool_shape
    updated_arr = np.zeros((avgpool_shape, avgpool_shape))

    while i < arr.shape[0]:
        # if the end of the matrix is reached, break
        if i + size > arr.shape[0]:
            break
        while j < arr.shape[1]:
            # if the end of the matrix is reached, break
            if j + size > arr.shape[1]:
                break
            # compute the average of the pooling matrix
            updated_arr[mat_i][mat_j] = int(np.average(arr[i : i + size, j : j + size]))
            # shift the pooling matrix by stride of column pixels
            j += stride
            mat_j += 1

        # shift the pooling matrix by stride of row pixels
        i += stride
        mat_i += 1
        # reset the column index to 0
        j = 0
        mat_j = 0

    return updated_arr


def validate_input(arr: np.ndarray, size: int, stride: int) -> None:
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    if size > arr.shape[0] or stride > arr.shape[1]:
        raise ValueError(
            "The size and stride must be lesser than or equal to the respective dimensions of the input array"
        )


def compute_output_shape(arr: np.ndarray, size: int, stride: int) -> tuple:
    return ((arr.shape[0] - size) // stride + 1, (arr.shape[1] - size) // stride + 1)


# Main Function
if __name__ == "__main__":
    from doctest import testmod

    testmod(name="avgpooling", verbose=True)

    # Loading the image
    image = Image.open("path_to_image")

    # Converting the image to numpy array and maxpooling, displaying the result
    # Ensure that the image is a square matrix

    Image.fromarray(maxpooling(np.array(image), size=3, stride=2)).show()

    # Converting the image to numpy array and averagepooling, displaying the result
    # Ensure that the image is a square matrix

    Image.fromarray(avgpooling(np.array(image), size=3, stride=2)).show()
