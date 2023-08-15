#!/usr/bin/env python3

"""
Implementation of entropy of information
https://en.wikipedia.org/wiki/Entropy_(information_theory)
"""
from __future__ import annotations

import math
from collections import Counter
from string import ascii_lowercase


from typing import Dict

def calculate_prob(text: str) -> None:
    single_char_strings, two_char_strings = analyze_text(text)

    entropy_single_chars = calculate_entropy(single_char_strings)
    entropy_double_chars = calculate_entropy(two_char_strings, is_double=True)
    difference_in_entropy = round(entropy_double_chars - entropy_single_chars, 1)

    print(f"{entropy_single_chars:.1f}")
    print(f"{entropy_double_chars:.1f}")
    print(f"{difference_in_entropy:.1f}")


def analyze_text(text: str) -> tuple[dict, dict]:
    """
    Convert text input into two dicts of counts.
    The first dictionary stores the frequency of single character strings.
    The second dictionary stores the frequency of two character strings.
    """
    single_char_strings = Counter()  # type: ignore
    two_char_strings = Counter()  # type: ignore
    single_char_strings[text[-1]] += 1

    # first case when we have space at start.
    two_char_strings[" " + text[0]] += 1
    for i in range(0, len(text) - 1):
        single_char_strings[text[i]] += 1
        two_char_strings[text[i : i + 2]] += 1
    return single_char_strings, two_char_strings


def calculate_entropy(
    strings_dictionary: dict[str, int], is_double: bool = False
) -> float:
    """
    Given a dictionary where keys are strings (single or double character)
    and values are counts, calculate the entropy.
    """
    my_alphas = list(" " + ascii_lowercase)
    total_sum = sum(strings_dictionary.values())
    entropy_sum = 0.0

    for ch0 in my_alphas:
        for ch1 in my_alphas if is_double else [""]:
            sequence = ch0 + ch1
            if sequence in strings_dictionary:
                probability = strings_dictionary[sequence] / total_sum
                entropy_sum += probability * math.log2(probability)

    return round(-1 * entropy_sum, 1)


def main():
    import doctest

    doctest.testmod()
    # text = (
    #     "Had repulsive dashwoods suspicion sincerity but advantage now him. Remark "
    #     "easily garret nor nay. Civil those mrs enjoy shy fat merry. You greatest "
    #     "jointure saw horrible. He private he on be imagine suppose. Fertile "
    #     "beloved evident through no service elderly is. Blind there if every no so "
    #     "at. Own neglected you preferred way sincerity delivered his attempted. To "
    #     "of message cottage windows do besides against uncivil.  Delightful "
    #     "unreserved impossible few estimating men favourable see entreaties. She "
    #     "propriety immediate was improving. He or entrance humoured likewise "
    #     "moderate. Much nor game son say feel. Fat make met can must form into "
    #     "gate. Me we offending prevailed discovery. "
    # )

    # calculate_prob(text)


if __name__ == "__main__":
    main()
