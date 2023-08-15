"""
A Hamming number is a positive integer of the form 2^i*3^j*5^k, for some
non-negative integers i, j, and k. They are often referred to as regular numbers.
More info at: https://en.wikipedia.org/wiki/Regular_number.
"""


from typing import List, Generator

def hamming(n_element: int) -> List[int]:
    """
    Generates a list of the first n_elements of the Hamming sequence.
    """
    if n_element < 1:
        raise ValueError("n_element should be a positive integer")

    hamming_gen = hamming_generator()
    hamming_list = [next(hamming_gen) for _ in range(n_element)]
    return hamming_list


if __name__ == "__main__":
    n = input("Enter the last number (nth term) of the Hamming Number Series: ")
    print("Formula of Hamming Number Series => 2^i * 3^j * 5^k")
    hamming_numbers = hamming(int(n))
    print("-----------------------------------------------------")
    print(f"The list with nth numbers is: {hamming_numbers}")
    print("-----------------------------------------------------")


def hamming_generator() -> Generator[int, None, None]:
    """
    Generator that yields the next number in the Hamming sequence.
    """

    hamming_list = [1]
    i, j, k = (0, 0, 0)

    while True:
        yield hamming_list[-1]
        while hamming_list[i] * 2 <= hamming_list[-1]:
            i += 1
        while hamming_list[j] * 3 <= hamming_list[-1]:
            j += 1
        while hamming_list[k] * 5 <= hamming_list[-1]:
            k += 1
        next_hamming = min(
            hamming_list[i] * 2, hamming_list[j] * 3, hamming_list[k] * 5
        )
        hamming_list.append(next_hamming)
