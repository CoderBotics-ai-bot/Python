"""
Author  : Alexander Pantyukhin
Date    : December 12, 2022

Task:
Given a string and a list of words, return true if the string can be
segmented into a space-separated sequence of one or more words.

Note that the same word may be reused
multiple times in the segmentation.

Implementation notes: Trie + Dynamic programming up -> down.
The Trie will be used to store the words. It will be useful for scanning
available words for the current position in the string.

Leetcode:
https://leetcode.com/problems/word-break/description/

Runtime: O(n * n)
Space: O(n)
"""

import functools
from typing import Any
from typing import Any, List


from typing import Any, List


def word_break(string: str, words: List[str]) -> bool:
    """
    Function to check whether a string can be segmented into words.
    string (str): input string.
    words (List[str]): list of words (dictionary).
    Returns:
    bool: True if string can be segmented, otherwise False.
    """
    validate_inputs(string, words)
    trie = build_trie(words)
    return is_breakable(string, trie)


if __name__ == "__main__":
    import doctest

    doctest.testmod()



def build_trie(words: List[str]) -> dict[str, Any]:
    """
    Build a trie data structure from the given list of words.
    words (List[str]): list of words.
    Returns:
    trie: a trie data structure.
    """
    trie: dict[str, Any] = {}
    for word in words:
        trie_node = trie
        for char in word:
            if char not in trie_node:
                trie_node[char] = {}
            trie_node = trie_node[char]
        trie_node["WORD_KEEPER"] = True
    return trie


def is_breakable(string: str, trie: dict[str, Any], index: int = 0) -> bool:
    """
    Recursively check if the string can be segmented into the words in trie.
    string (str): the input string.
    trie (dict[str, Any]): the trie built from the dictionary of words.
    index (int): current index of string.
    Returns:
    bool: True if string can be segmented, otherwise False.
    """
    if index == len(string):
        return True

    trie_node = trie
    for i in range(index, len(string)):
        trie_node = trie_node.get(string[i], None)
        if trie_node is None:
            return False
        if trie_node.get("WORD_KEEPER", False) and is_breakable(string, trie, i + 1):
            return True
    return False


def validate_inputs(string: str, words: List[str]) -> None:
    """
    Validates the inputs of the word_break function.
    string (str): input string.
    words (List[str]): list of words (dictionary).
    Raises:
    ValueError: If the input 'string' or 'words' is invalid.
    """
    if not string:
        raise ValueError("Input string is empty")
    if not words or not all(words):
        raise ValueError("Word dictionary is empty")
