"""
    One of the several implementations of Lempel–Ziv–Welch decompression algorithm
    https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
"""

import math
import sys


def read_file_binary(file_path: str) -> str:
    """
    Reads given file as bytes and returns them as a long string
    """
    result = ""
    try:
        with open(file_path, "rb") as binary_file:
            data = binary_file.read()
        for dat in data:
            curr_byte = f"{dat:08b}"
            result += curr_byte
        return result
    except OSError:
        print("File not accessible")
        sys.exit()

def decompress_data(data_bits: str) -> str:
    """
    Decompresses the given data_bits using the Lempel-Ziv-Welch (LZW) compression algorithm

    Args:
        data_bits: A string of binary data bits that represents compressed data.

    Returns:
        A string that represents the decompressed data.

    """

    lexicon = initialize_lexicon()
    result, curr_string, index = "", "", len(lexicon)

    for bit in data_bits:
        curr_string, result = add_bit_to_current_string(
            curr_string, bit, lexicon, result
        )
        lexicon, index = expand_lexicon_if_needed(lexicon, index, result)

    return result


def write_file_binary(file_path: str, to_write: str) -> None:
    """
    Writes given to_write string (should only consist of 0's and 1's) as bytes in the
    file
    """
    byte_length = 8
    try:
        with open(file_path, "wb") as opened_file:
            result_byte_array = [
                to_write[i : i + byte_length]
                for i in range(0, len(to_write), byte_length)
            ]

            if len(result_byte_array[-1]) % byte_length == 0:
                result_byte_array.append("10000000")
            else:
                result_byte_array[-1] += "1" + "0" * (
                    byte_length - len(result_byte_array[-1]) - 1
                )

            for elem in result_byte_array[:-1]:
                opened_file.write(int(elem, 2).to_bytes(1, byteorder="big"))
    except OSError:
        print("File not accessible")
        sys.exit()


def initialize_lexicon() -> dict:
    """
    Initializes the lexicon to begin the decompression.

    Returns:
        A dictionary acting as a lexicon for the decompression.

    """
    return {"0": "0", "1": "1"}


def add_bit_to_current_string(
    curr_string: str, bit: str, lexicon: dict, result: str
) -> tuple:
    """
    Adds the current bit to the current string and updates the result if the current string is
    in the lexicon.

    Args:
        curr_string: The current sequence.
        bit: The current bit.
        lexicon: The current lexicon.
        result: The current result.

    Returns:
        The updated current string and result.

    """
    curr_string += bit

    if curr_string in lexicon:
        last_match_id = lexicon[curr_string]
        result += last_match_id
        lexicon[curr_string] = last_match_id + "0"
        curr_string = ""

    return curr_string, result


def expand_lexicon_if_needed(lexicon: dict, index: int, result: str) -> tuple:
    """
    Expands the lexicon if needed and updates the index.

    Args:
        lexicon: The lexicon to potentially be expanded.
        index: The current index.
        result: The current result.

    Returns:
        The extended lexicon and updated index.

    """
    if math.log2(index).is_integer():
        lexicon = extend_lexicon(lexicon)

    last_match_id = result[-1] if len(result) else "0"
    lexicon[bin(index)[2:]] = last_match_id + "1"
    index += 1

    return lexicon, index


def extend_lexicon(lexicon: dict) -> dict:
    """
    Extends the lexicon by adding a "0" prefix to every key in the lexicon.

    Args:
        lexicon: The lexicon to be extended.

    Returns:
        The extended lexicon.

    """
    return {"0" + key: value for key, value in lexicon.items()}


def remove_prefix(data_bits: str) -> str:
    """
    Removes size prefix, that compressed file should have
    Returns the result
    """
    counter = 0
    for letter in data_bits:
        if letter == "1":
            break
        counter += 1

    data_bits = data_bits[counter:]
    data_bits = data_bits[counter + 1 :]
    return data_bits


def compress(source_path: str, destination_path: str) -> None:
    """
    Reads source file, decompresses it and writes the result in destination file
    """
    data_bits = read_file_binary(source_path)
    data_bits = remove_prefix(data_bits)
    decompressed = decompress_data(data_bits)
    write_file_binary(destination_path, decompressed)


if __name__ == "__main__":
    compress(sys.argv[1], sys.argv[2])
