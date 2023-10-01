# Source : https://computersciencewiki.org/index.php/Max-pooling_/_Pooling
# Importing the libraries
import numpy as np
from PIL import Image


import numpy as np


from typing import Tuple
from typing import List
from numpy import ndarray


from typing import Tuple, List

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


def avgpooling(arr: ndarray, size: int, stride: int) -> ndarray:
    """
    Perform average pooling on a 2D numpy array (image).

    ...

    """
    # Input validation
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")

    # compute the shape of the output matrix
    avgpool_shape = (arr.shape[0] - size) // stride + 1

    # initialize the output matrix with zeros of shape avgpool_shape
    updated_arr = np.zeros((avgpool_shape, avgpool_shape))

    for mat_i in range(0, arr.shape[0], stride):
        if mat_i + size > arr.shape[0]:
            break

        for mat_j in range(0, arr.shape[1], stride):
            if mat_j + size > arr.shape[1]:
                break

            # compute the average of the pooling matrix
            updated_arr[mat_i // stride][mat_j // stride] = int(
                compute_avg_pooling(arr, size, stride, mat_i, mat_j)
            )

    return updated_arr


def validate_input(arr: np.ndarray, size: int, stride: int) -> None:
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    if size > arr.shape[0] or stride > arr.shape[1]:
        raise ValueError(
            "The size and stride must be lesser than or equal to the respective dimensions of the input array"
        )

def compute_avg_pooling(
    arr: ndarray, size: int, stride: int, mat_i: int, mat_j: int
) -> float:
    """
    Compute the average of a sub-matrix of 'arr' with size 'size', starting from position (mat_i, mat_j), moving by 'stride' both vertically and horizontally.

    Args:
        arr (ndarray): Input 2D square image array.
        size (int): Size of the sub-matrix (pooling window).
        stride (int): Stride (step size) for moving the pooling window.
        mat_i (int): Vertical starting index.
        mat_j (int): Horizontal starting index.

    Returns:
        float: the average of the sub-matrix.
    """
    return np.average(arr[mat_i : mat_i + size : stride, mat_j : mat_j + size : stride])


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
