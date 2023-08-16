"""
A Hamming number is a positive integer of the form 2^i*3^j*5^k, for some
non-negative integers i, j, and k. They are often referred to as regular numbers.
More info at: https://en.wikipedia.org/wiki/Regular_number.
"""

def hamming(n_element: int) -> list:
    """
    Generate the first 'n_element' numbers in the Hamming sequence.

    The Hamming sequence is a strictly increasing sequence of numbers of the form 2**i * 3**j * 5**k, where
    i, j, k are non-negative integers.

    :param n_element: A positive integer indicating the number of Hamming numbers to generate.
    :type n_element: int
    :return: A list of the first 'n_element' Hamming numbers.
    :rtype: list
    :raise ValueError: If 'n_element' is less than 1.

    :Example:

    >>> hamming(5)
    [1, 2, 3, 4, 5]
    >>> hamming(10)
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    >>> hamming(15)
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]

    """
    n_element = int(n_element)
    if n_element < 1:
        raise ValueError("n_element should be a positive integer")

    hamming_list = [1]
    i, j, k = 0, 0, 0
    while len(hamming_list) < n_element:
        min_val = min(hamming_list[i] * 2, hamming_list[j] * 3, hamming_list[k] * 5)
        if min_val > hamming_list[-1]:
            hamming_list.append(min_val)
        if min_val == hamming_list[i] * 2:
            i += 1
        if min_val == hamming_list[j] * 3:
            j += 1
        if min_val == hamming_list[k] * 5:
            k += 1

    return hamming_list


if __name__ == "__main__":
    n = input("Enter the last number (nth term) of the Hamming Number Series: ")
    print("Formula of Hamming Number Series => 2^i * 3^j * 5^k")
    hamming_numbers = hamming(int(n))
    print("-----------------------------------------------------")
    print(f"The list with nth numbers is: {hamming_numbers}")
    print("-----------------------------------------------------")
