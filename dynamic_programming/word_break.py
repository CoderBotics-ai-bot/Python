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


from typing import List, Any


def word_break(string: str, words: list[str]) -> bool:
    """
    Checks if a given string can be segmented into a space-separated
    sequence of one or more dictionary words. Utilizes dynamic programming
    and trie data structure to improve efficiency.
    """

    # Validate first, exit if invalid
    input_validation(string, words)

    # Build the trie
    trie = build_trie(words)

    # Initialize length variable
    len_string = len(string)

    # Initialize is_breakable function
    @functools.cache
    def is_breakable(index: int) -> bool:
        # Scroll the string
        if index == len_string:
            return True

        trie_node = trie
        for i in range(index, len_string):
            trie_node = trie_node.get(string[i], None)

            # Scroll the trie, exit if necessary
            if trie_node is None:
                return False

            if trie_node.get("WORD_KEEPER", False) and is_breakable(i + 1):
                return True

        # Default return
        return False

    return is_breakable(0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

def input_validation(string: str, words: List[str]) -> None:
    """Validates the inputs."""

    if not isinstance(string, str) or len(string) == 0:
        raise ValueError("the string should be not an empty string")

    if not isinstance(words, list) or not all(
        isinstance(item, str) and len(item) > 0 for item in words
    ):
        raise ValueError("the words should be a list of non-empty strings")


def build_trie(words: List[str]) -> dict[str, Any]:
    """Builds the trie data structure for given words."""

    # Initialize an empty trie
    trie: dict[str, Any] = {}
    word_keeper_key = "WORD_KEEPER"

    # Adding words to trie
    for word in words:
        trie_node = trie
        for c in word:
            if c not in trie_node:
                trie_node[c] = {}

            trie_node = trie_node[c]

        trie_node[word_keeper_key] = True

    return trie
