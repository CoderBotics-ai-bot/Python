"""
The nested brackets problem is a problem that determines if a sequence of
brackets are properly nested.  A sequence of brackets s is considered properly nested
if any of the following conditions are true:

        - s is empty
        - s has the form (U) or [U] or {U} where U is a properly nested string
        - s has the form VW where V and W are properly nested strings

For example, the string "()()[()]" is properly nested but "[(()]" is not.

The function called is_balanced takes as input a string S which is a sequence of
brackets and returns true if S is nested and false otherwise.
"""

def is_balanced(s: str) -> bool:
    """
    Check if the given string of brackets is balanced.

    This function checks if the given string of brackets is balanced, i.e.
    any open bracket has a corresponding closing bracket and brackets are properly nested.

    Arguments:
    s -- The string of brackets to be checked.

    Returns:
    True if the given string of brackets is balanced, False otherwise.
    """
    stack = []
    brackets_mapping = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if char in brackets_mapping.values():
            stack.append(char)
        elif char in brackets_mapping.keys():
            if not stack or brackets_mapping[char] != stack.pop():
                return False

    return not stack


def main():
    s = input("Enter sequence of brackets: ")
    if is_balanced(s):
        print(s, "is balanced")
    else:
        print(s, "is not balanced")


if __name__ == "__main__":
    main()
