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


def rgb_to_hsv(red: int, green: int, blue: int) -> list[float]:
    """
    Conversion from the RGB-representation to the HSV-representation.
    The tested values are the reverse values from the hsv_to_rgb-doctests.
    Function "approximately_equal_hsv" is needed because of small deviations due to
    rounding for the RGB-values.

    >>> approximately_equal_hsv(rgb_to_hsv(0, 0, 0), [0, 0, 0])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 255, 255), [0, 0, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 0, 0), [0, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 255, 0), [60, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(0, 255, 0), [120, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(0, 0, 255), [240, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(255, 0, 255), [300, 1, 1])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(64, 128, 128), [180, 0.5, 0.5])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(193, 196, 224), [234, 0.14, 0.88])
    True
    >>> approximately_equal_hsv(rgb_to_hsv(128, 32, 80), [330, 0.75, 0.5])
    True
    """
    if red < 0 or red > 255:
        raise Exception("red should be between 0 and 255")

    if green < 0 or green > 255:
        raise Exception("green should be between 0 and 255")

    if blue < 0 or blue > 255:
        raise Exception("blue should be between 0 and 255")

    float_red = red / 255
    float_green = green / 255
    float_blue = blue / 255
    value = max(float_red, float_green, float_blue)
    chroma = value - min(float_red, float_green, float_blue)
    saturation = 0 if value == 0 else chroma / value

    if chroma == 0:
        hue = 0.0
    elif value == float_red:
        hue = 60 * (0 + (float_green - float_blue) / chroma)
    elif value == float_green:
        hue = 60 * (2 + (float_blue - float_red) / chroma)
    else:
        hue = 60 * (4 + (float_red - float_green) / chroma)

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
