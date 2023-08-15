from __future__ import annotations

from collections.abc import Sequence
from typing import Literal


def compare_string(string1: str, string2: str) -> str | Literal[False]:
    """
    >>> compare_string('0010','0110')
    '0_10'

    >>> compare_string('0110','1101')
    False
    """
    list1 = list(string1)
    list2 = list(string2)
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
            list1[i] = "_"
    if count > 1:
        return False
    else:
        return "".join(list1)


def check(binary: list[str]) -> list[str]:
    """
    >>> check(['0.00.01.5'])
    ['0.00.01.5']
    """
    pi = []
    while True:
        check1 = ["$"] * len(binary)
        temp = []
        for i in range(len(binary)):
            for j in range(i + 1, len(binary)):
                k = compare_string(binary[i], binary[j])
                if k is False:
                    check1[i] = "*"
                    check1[j] = "*"
                    temp.append("X")
        for i in range(len(binary)):
            if check1[i] == "$":
                pi.append(binary[i])
        if len(temp) == 0:
            return pi
        binary = list(set(temp))


def decimal_to_binary(no_of_variable: int, minterms: Sequence[float]) -> list[str]:
    """
    >>> decimal_to_binary(3,[1.5])
    ['0.00.01.5']
    """
    temp = []
    for minterm in minterms:
        string = ""
        for _ in range(no_of_variable):
            string = str(minterm % 2) + string
            minterm //= 2
        temp.append(string)
    return temp


def is_for_table(string1: str, string2: str, count: int) -> bool:
    """
    >>> is_for_table('__1','011',2)
    True

    >>> is_for_table('01_','001',1)
    False
    """
    list1 = list(string1)
    list2 = list(string2)
    count_n = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count_n += 1
    return count_n == count


def selection(chart: list[list[int]], prime_implicants: list[str]) -> list[str]:
    """
    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']

    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']
    """
    temp = []
    select = [0] * len(chart)
    for i in range(len(chart[0])):
        count = 0
        rem = -1
        for j in range(len(chart)):
            if chart[j][i] == 1:
                count += 1
                rem = j
        if count == 1:
            select[rem] = 1
    for i in range(len(select)):
        if select[i] == 1:
            for j in range(len(chart[0])):
                if chart[i][j] == 1:
                    for k in range(len(chart)):
                        chart[k][j] = 0
            temp.append(prime_implicants[i])
    while True:
        max_n = 0
        rem = -1
        count_n = 0
        for i in range(len(chart)):
            count_n = chart[i].count(1)
            if count_n > max_n:
                max_n = count_n
                rem = i

        if max_n == 0:
            return temp

        temp.append(prime_implicants[rem])

        for i in range(len(chart[0])):
            if chart[rem][i] == 1:
                for j in range(len(chart)):
                    chart[j][i] = 0



def prime_implicant_chart(
    prime_implicants: Sequence[str], binary: Sequence[str]
) -> list[list[int]]:
    """
    Generate a prime implicant chart given prime implicants and binary strings.

    This function creates a prime implicant chart which is a 2D list of integers,
    by comparing each prime implicant with each binary string.
    If the number of mismatching characters in the prime implicant and binary string is
    equal to the count of underscore("_") in the prime implicant, then it is a match (1),
    otherwise no match (0).

    Args:
        prime_implicants (Sequence[str]): A sequence of prime implicant strings.
        binary (Sequence[str]): A sequence of binary strings.

    Returns:
        list[list[int]]: The generated 2D prime implicant chart,
                          where rows correspond to prime implicants and columns to binary strings.

    Examples:
        >>> prime_implicant_chart(['0.00.01.5'],['0.00.01.5'])
        [[1]]
    """
    underscore_counts = list(
        map(str.count, prime_implicants, ["_"] * len(prime_implicants))
    )
    return [
        [int(is_for_table(p, b, u)) for b in binary]
        for p, u in zip(prime_implicants, underscore_counts)
    ]


def main() -> None:
    no_of_variable = int(input("Enter the no. of variables\n"))
    minterms = [
        float(x)
        for x in input(
            "Enter the decimal representation of Minterms 'Spaces Separated'\n"
        ).split()
    ]
    binary = decimal_to_binary(no_of_variable, minterms)

    prime_implicants = check(binary)
    print("Prime Implicants are:")
    print(prime_implicants)
    chart = prime_implicant_chart(prime_implicants, binary)

    essential_prime_implicants = selection(chart, prime_implicants)
    print("Essential Prime Implicants are:")
    print(essential_prime_implicants)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
