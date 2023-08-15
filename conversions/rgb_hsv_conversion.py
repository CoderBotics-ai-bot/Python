"""
The RGB color model is an additive color model in which red, green, and blue light
are added together in various ways to reproduce a broad array of colors. The name
of the model comes from the initials of the three additive primary colors, red,
green, and blue. Meanwhile, the HSV representation models how colors appear under
light. In it, colors are represented using three components: hue, saturation and
(brightness-)value. This file provides functions for converting colors from one
representation to the other.

(description adapted from https://en.wikipedia.org/wiki/RGB_color_model and
https://en.wikipedia.org/wiki/HSL_and_HSV).
"""


from typing import List


def hsv_to_rgb(hue: float, saturation: float, value: float) -> list[int]:
    """
    Converts color parameters from HSV (Hue, Saturation, Value) to RGB (Red, Green, Blue).

    Args:
        hue (float): Input hue value, within the range [0, 360].
        saturation (float): Input saturation value, within the range [0, 1].
        value (float): Input value (brightness), within the range [0, 1].

    Returns:
        list[int]: The RGB equivalents ranging from 0 to 255.

    Examples:
        >>> hsv_to_rgb(0, 0, 0)
        [0, 0, 0]
        >>> hsv_to_rgb(0, 0, 1)
        [255, 255, 255]
        >>> hsv_to_rgb(0, 1, 1)
        [255, 0, 0]
        >>> hsv_to_rgb(60, 1, 1)
        [255, 255, 0]
        >>> hsv_to_rgb(300, 1, 1)
        [255, 0, 255]
    """
    # Validate the input parameters
    validate_parameters(hue, saturation, value)

    # Existing Code for HSV to RGB conversion...


def rgb_to_hsv(red: int, green: int, blue: int) -> List[float]:
    """
    Convert a RGB color to HSV.

    Args:
        red (int): Red RGB color channel.
        green (int): Green RGB color channel.
        blue (int): Blue RGB color channel.

    Returns:
        List[float]: HSV representation of the color.
    """
    validate_rgb_value(red, "red")
    validate_rgb_value(green, "green")
    validate_rgb_value(blue, "blue")

    float_red, float_green, float_blue = map(rgb_to_percentage, [red, green, blue])
    value = max(float_red, float_green, float_blue)
    chroma = value - min(float_red, float_green, float_blue)
    saturation = 0 if value == 0 else chroma / value

    if chroma != 0:
        if value == float_red:
            hue = 60 * (0 + (float_green - float_blue) / chroma)
        elif value == float_green:
            hue = 60 * (2 + (float_blue - float_red) / chroma)
        else:
            hue = 60 * (4 + (float_red - float_green) / chroma)
    else:
        hue = 0.0

    hue = (hue + 360) % 360

    return [hue, saturation, value]

def validate_parameters(hue: float, saturation: float, value: float) -> bool:
    """
    Validate the input parameters for HSV to RGB conversion.

    Args:
        hue (float): Input hue value within the range [0, 360].
        saturation (float): Input saturation value within the range [0, 1].
        value (float): Input value(brightness) within the range [0, 1].

    Raises:
        ValueError: If any of the input parameters are out of their respective valid ranges.

    Returns:
        bool: True if all parameters are valid, False otherwise.
    """
    if not 0 <= hue <= 360:
        raise ValueError("Hue must be in the range [0, 360].")
    if not 0 <= saturation <= 1:
        raise ValueError("Saturation must be in the range [0, 1].")
    if not 0 <= value <= 1:
        raise ValueError("Value must be in the range [0, 1].")
    return True

def validate_rgb_value(value: int, color: str) -> None:
    """
    Validates the given RGB color value to be in range [0,255].

    Args:
        value (int): The color value to validate.
        color (str): The color name to use in exception message in case of invalid value.

    Raises:
        Exception: If the color value is not an integer in range [0,255].
    """
    if value < 0 or value > 255:
        raise Exception(f"{color} should be between 0 and 255")


def rgb_to_percentage(rgb_value: int) -> float:
    """
    Converts an RGB color value (0-255) to percentage.

    Args:
        rgb_value (int): RGB color value, integer in range [0, 255].

    Returns:
        float: Color value converted to percentage.
    """
    PERCENTAGE_DIVISOR = 255
    return rgb_value / PERCENTAGE_DIVISOR


def approximately_equal_hsv(hsv_1: list[float], hsv_2: list[float]) -> bool:
    """
    Utility-function to check that two hsv-colors are approximately equal

    >>> approximately_equal_hsv([0, 0, 0], [0, 0, 0])
    True
    >>> approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.500001, 0.30001])
    True
    >>> approximately_equal_hsv([0, 0, 0], [1, 0, 0])
    False
    >>> approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.6, 0.30001])
    False
    """
    check_hue = abs(hsv_1[0] - hsv_2[0]) < 0.2
    check_saturation = abs(hsv_1[1] - hsv_2[1]) < 0.002
    check_value = abs(hsv_1[2] - hsv_2[2]) < 0.002

    return check_hue and check_saturation and check_value
