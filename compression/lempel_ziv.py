"""
    One of the several implementations of Lempel–Ziv–Welch compression algorithm
    https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
"""

import math
import os
import sys


from typing import Tuple, Dict


from typing import List


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


def add_key_to_lexicon(
    lexicon: dict[str, str], curr_string: str, index: int, last_match_id: str
) -> None:
    """
    Adds new strings (curr_string + "0",  curr_string + "1") to the lexicon
    """
    lexicon.pop(curr_string)
    lexicon[curr_string + "0"] = last_match_id

    if math.log2(index).is_integer():
        for curr_key in lexicon:
            lexicon[curr_key] = "0" + lexicon[curr_key]

    lexicon[curr_string + "1"] = bin(index)[2:]

def compress_data(data_bits: str) -> str:
    lexicon = initialize_lexicon()
    compressed_data, remainder = compress_bits(data_bits, lexicon)
    if remainder:
        compressed_data += process_remainder(remainder, lexicon)
    return compressed_data


def add_file_length(source_path: str, compressed: str) -> str:
    """
    Adds given file's length in front (using Elias  gamma coding) of the compressed
    string
    """
    file_length = os.path.getsize(source_path)
    file_length_binary = bin(file_length)[2:]
    length_length = len(file_length_binary)

    return "0" * (length_length - 1) + file_length_binary + compressed

def write_file_binary(file_path: str, to_write: str) -> None:
    """
    Writes given binary string to a file as bytes.

    Args:
        file_path (str): Path to the file where bytes will be written.
        to_write (str): Binary string that will be written in the file as bytes.
                        Should only consist of '0' and '1'.

    Raises:
        OSError: If the file specified by file_path is not accessible.
        SystemExit: If the OSError is raised.
    """
    byte_length = 8
    try:
        with open(file_path, "wb") as opened_file:
            write_bytes_array_to_file(
                convert_string_to_byte_array(to_write, byte_length), opened_file
            )
    except OSError:
        print("File not accessible")
        sys.exit()


def initialize_lexicon() -> dict[str, str]:
    return {"0": "0", "1": "1"}


def convert_string_to_byte_array(binary_data: str, byte_length: int) -> List[str]:
    """
    Convert a binary string into a list of bytes (as strings).

    Args:
        binary_data (str): Binary string to be converted.
        byte_length (int): Length of a byte in bits.

    Returns:
        List of bytes (as strings).
    """
    byte_array = [
        binary_data[i : i + byte_length]
        for i in range(0, len(binary_data), byte_length)
    ]
    return pad_incomplete_byte(byte_array, byte_length)


def pad_incomplete_byte(byte_array: List[str], byte_length: int) -> List[str]:
    """
    Pad incomplete byte with required number of bits.

    Args:
        byte_array (List[str]): Array with bytes represented as strings.
        byte_length (int): Length of a byte in bits.

    Returns:
        Array with padded incomplete byte.
    """
    last_byte = byte_array[-1]
    if len(last_byte) % byte_length == 0:
        byte_array.append("10000000")
    else:
        byte_array[-1] = last_byte + "1" + "0" * (byte_length - len(last_byte) - 1)

    return byte_array


def write_bytes_array_to_file(byte_array: List[str], file_object) -> None:
    """
    Write an array of bytes to a file.

    Args:
        byte_array (List[str]): Array with bytes represented as strings.
        file_object: Object representing a file where to write bytes.
    """
    for byte in byte_array:
        file_object.write(int(byte, 2).to_bytes(1, byteorder="big"))


def compress_bits(data_bits: str, lexicon: dict[str, str]) -> Tuple[str, str]:
    index = len(lexicon)
    result, curr_string = "", ""
    for i in range(len(data_bits)):
        curr_string += data_bits[i]
        if curr_string not in lexicon:
            continue
        result += lexicon[curr_string]
        add_key_to_lexicon(lexicon, curr_string, index, lexicon[curr_string])
        index += 1
        curr_string = ""
    return result, curr_string


def process_remainder(remainder: str, lexicon: dict[str, str]) -> str:
    while remainder and remainder not in lexicon:
        remainder += "0"
    return lexicon[remainder] if remainder else ""


def compress(source_path: str, destination_path: str) -> None:
    """
    Reads source file, compresses it and writes the compressed result in destination
    file
    """
    data_bits = read_file_binary(source_path)
    compressed = compress_data(data_bits)
    compressed = add_file_length(source_path, compressed)
    write_file_binary(destination_path, compressed)


if __name__ == "__main__":
    compress(sys.argv[1], sys.argv[2])
