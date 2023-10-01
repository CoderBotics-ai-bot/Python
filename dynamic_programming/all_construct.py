"""
Program to list all the ways a target string can be
constructed from the given list of substrings
"""
from __future__ import annotations


def all_construct(target: str, word_bank: list[str] | None = None) -> list[list[str]]:
    """
    Returns all the possible combinations a string can be constructed from given substrings.
    """

    word_bank = word_bank or []
    table_size: int = len(target) + 1

    # Initialize the table with empty lists
    table: list[list[list[str]]] = [[] for _ in range(table_size)]

    # Add the combination for an empty string
    table[0] = [[]]

    # Iterate through the indices
    for i in range(table_size):
        if table[i]:  # If there is at least one combination at the current index
            gather_targets(target, word_bank, i, table)

    # Reverse the final combinations for better output
    for combination in table[len(target)]:
        combination.reverse()

    return table[len(target)]


if __name__ == "__main__":
    print(all_construct("jwajalapa", ["jwa", "j", "w", "a", "la", "lapa"]))
    print(all_construct("rajamati", ["s", "raj", "amat", "raja", "ma", "i", "t"]))
    print(
        all_construct(
            "hexagonosaurus",
            ["h", "ex", "hex", "ag", "ago", "ru", "auru", "rus", "go", "no", "o", "s"],
        )
    )

def gather_targets(
    target: str, word_bank: list[str], index: int, table: list[list[list[str]]]
) -> None:
    """
    Helper function to populate the table with all possible combinations at a particular index.
    """

    for word in word_bank:
        if target[index : index + len(word)] == word:
            # Get all the combinations for the current word
            new_combinations = [[word, *combination] for combination in table[index]]

            # Update the table using the combinations found
            table[index + len(word)].extend(new_combinations)
