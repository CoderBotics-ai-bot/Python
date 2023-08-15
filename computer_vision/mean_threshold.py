from PIL import Image


from typing import List

"""
Mean thresholding algorithm for image processing
https://en.wikipedia.org/wiki/Thresholding_(image_processing)
"""


def mean_threshold(image: Image) -> Image:
    """
    Takes a grayscale PIL image and applies mean thresholding to it.

    This function works by first calculating the mean value of the grayscale intensities in the image.
    Then, for each pixel in the image, it sets the pixel to the maximum value (white) if the pixel's
    intensity is greater than the mean, else it sets the pixel to the minimum value (black).

    Args:
        image: A PIL image in grayscale.

    Returns:
        The thresholded grayscale image.
    """
    threshold = calculate_mean(image)
    apply_threshold(image, threshold)
    return image


if __name__ == "__main__":
    image = mean_threshold(Image.open("path_to_image").convert("L"))
    image.save("output_image_path")

def calculate_mean(image: Image) -> int:
    """
    Calculate mean brightness of image.

    Args:
        image: A PIL image in grayscale.

    Returns:
        Mean value of image brightness.
    """
    width, height = image.size
    pixels = image.load()
    total_brightness = sum(pixels[j, i] for i in range(height) for j in range(width))
    return total_brightness // (width * height)


def apply_threshold(image: Image, threshold: int) -> None:
    """
    Apply mean threshold on image.

    Args:
        image: A PIL image in grayscale.
        threshold: Value of brightness threshold.
    """
    width, height = image.size
    pixels = image.load()
    for i in range(height):
        for j in range(width):
            pixels[j, i] = 255 if pixels[j, i] > threshold else 0
