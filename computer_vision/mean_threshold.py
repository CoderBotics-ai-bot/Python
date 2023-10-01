from PIL import Image

"""
Mean thresholding algorithm for image processing
https://en.wikipedia.org/wiki/Thresholding_(image_processing)
"""

def mean_threshold(image: Image) -> Image:
    """
    Apply a mean threshold filter on a grayscale PIL image.

    Args:
        image (PIL.Image): A grayscale Pillow Image object.

    Returns:
        PIL.Image: A binary image where pixels with a value above the mean are white, and the rest black.

    """
    pixels = image.load()
    width, height = image.size

    mean_pixel_value = get_mean_pixel_value(pixels, width, height)
    apply_threshold(pixels, mean_pixel_value, width, height)

    return image


if __name__ == "__main__":
    image = mean_threshold(Image.open("path_to_image").convert("L"))
    image.save("output_image_path")


def get_mean_pixel_value(pixels, width: int, height: int) -> int:
    total_pixel_value = sum(pixels[i, j] for j in range(width) for i in range(height))
    return total_pixel_value // (width * height)


def apply_threshold(pixels, threshold: int, width: int, height: int):
    for j in range(width):
        for i in range(height):
            pixels[i, j] = 255 if pixels[i, j] > threshold else 0
