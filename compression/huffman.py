from __future__ import annotations

import sys


from typing import List


from typing import Dict, Union


class Letter:
    def __init__(self, letter: str, freq: int):
        self.letter: str = letter
        self.freq: int = freq
        self.bitstring: dict[str, str] = {}

    def __repr__(self) -> str:
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq: int, left: Letter | TreeNode, right: Letter | TreeNode):
        self.freq: int = freq
        self.left: Letter | TreeNode = left
        self.right: Letter | TreeNode = right


def parse_file(file_path: str) -> List[Letter]:
    """
    Parse a file and return a sorted list of Letter objects.

    Args:
        file_path (str): The path to the file.

    Returns:
        List[Letter]: A sorted list of Letter objects representing each character
                      in the file sorted by frequency.
    """
    char_freq = _get_char_freq(file_path)
    letters = [Letter(char, freq) for char, freq in char_freq.items()]
    return sorted(letters, key=lambda letter: letter.freq)


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    """
    Run through the list of Letters and build the min heap
    for the Huffman Tree.
    """
    response: list[Letter | TreeNode] = letters  # type: ignore
    while len(response) > 1:
        left = response.pop(0)
        right = response.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    return response[0]

def _get_char_freq(file_path: str) -> dict[str, int]:
    """
    Extracts characters from a file and calculates their frequency.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict[str, int]: A dictionary mapping each character to its frequency.
    """
    char_freq = {}
    with open(file_path) as input_file:
        while True:
            char = input_file.read(1)
            if not char:
                break
            char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq


def traverse_tree(root: Letter | TreeNode, bitstring: str) -> list[Letter]:
    """
    Recursively traverse the Huffman Tree to set each
    Letter's bitstring dictionary, and return the list of Letters
    """
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root  # type: ignore
    letters = []
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    return letters

def huffman(file_path: str) -> None:
    """
    Run the Huffman coding algorithm on a given file.

    This function carries out the Huffman coding algorithm on a file.
    The steps involved in the algorithm are:

    1. Parse the file and create a list of Letter objects.
    2. Build a Huffman Tree with the Letter objects.
    3. Assign a unique bitstring to each Letter object.
    4. Display the bitstring associated with each character.

    Args:
        file_path (str): The path of the file to encode using Huffman coding.

    Raises:
        IOError: If the file is not accessible.
    """
    letters_list = parse_file(file_path)
    root = build_tree(letters_list)
    letters = extract_bitstrings(root)
    display_coding(file_path, letters)


if __name__ == "__main__":
    # pass the file path to the huffman function
    huffman(sys.argv[1])


def extract_bitstrings(root: Union[Letter, TreeNode]) -> Dict[str, str]:
    return {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }


def display_coding(file_path: str, letters: Dict[str, str]) -> None:
    print(f"Huffman Coding  of {file_path}: ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(letters[c], end=" ")
    print("\n")
