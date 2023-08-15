"""
Sum of digits sequence
Problem 551

Let a(0), a(1),... be an integer sequence defined by:
     a(0) = 1
     for n >= 1, a(n) is the sum of the digits of all preceding terms

The sequence starts with 1, 1, 2, 4, 8, ...
You are given a(10^6) = 31054319.

Find a(10^15)
"""


from typing import List, Tuple, Optional


ks = range(2, 20 + 1)
base = [10**k for k in range(ks[-1] + 1)]
memo: dict[int, dict[int, list[list[int]]]] = {}

def next_term(a_i: List[int], k: int, i: int, n: int) -> Tuple[int, int]:
    """
    Calculate and update given sequence in place up to the nth term or until c > 10^k
    with terms written in the form: a(i) = b * 10^k + c

    For any a(i), if digitsum(b) and c have the same value, the difference between subsequent
    terms will be the same until c >= 10^k. The difference is cached to speed up computation.
    This updates a_i to either the n-th term or the smallest term for which c > 10^k.

    Args:
    a_i (List[int]): A list of integers representing the i-th term in the sequence.
    k (int): Kth position along the sequence.
    i (int): Starting position along the sequence.
    n (int): End position along the sequence.

    Returns:
    Tuple[int, int]: A tuple with difference between the ending term and starting term, and
                     the number of terms calculated. If the starting term is a_0=1 and
                     ending term is a_10=62, then (61, 9) is returned.
    """
    difference, ct = get_difference_and_ct(a_i, k, i)
    while ct < n and a_i[-1] < base[k + 1]:
        if difference is None:
            a_i.append(a_i[-1] + 1)
            difference, ct = get_difference_and_ct(
                a_i, k, calc_base_k_plus_one_index(ct)
            )
        else:
            a_i.append(a_i[-1] + difference)
            ct += 1
    return a_i[-1] - a_i[i], ct - i


def compute(a_i, k, i, n):
    """
    same as next_term(a_i, k, i, n) but computes terms without memoizing results.
    """
    if i >= n:
        return 0, i
    if k > len(a_i):
        a_i.extend([0 for _ in range(k - len(a_i))])

    # note: a_i -> b * 10^k + c
    # ds_b -> digitsum(b)
    # ds_c -> digitsum(c)
    start_i = i
    ds_b, ds_c, diff = 0, 0, 0
    for j in range(len(a_i)):
        if j >= k:
            ds_b += a_i[j]
        else:
            ds_c += a_i[j]

    while i < n:
        i += 1
        addend = ds_c + ds_b
        diff += addend
        ds_c = 0
        for j in range(k):
            s = a_i[j] + addend
            addend, a_i[j] = divmod(s, 10)

            ds_c += a_i[j]

        if addend > 0:
            break

    if addend > 0:
        add(a_i, k, addend)
    return diff, i - start_i


def get_difference_and_ct(a_i: List[int], k: int, i: int) -> Tuple[Optional[int], int]:
    """
    Calculate difference and ct based on the given sequence and kth position.

    Args:
    a_i (List[int]): A list of integers representing the i-th term in the sequence.
    k (int): Kth position along the sequence.
    i (int): Starting position along the sequence.

    Returns:
    Tuple[Optional[int], int]: A tuple with the difference between the ending term and starting term if
                               it's found in the memo, and the number of terms calculated. Returns
                               None instead of a difference if it's not found in the memo.
    """
    ct = i
    difference = None
    if k in memo and i in memo[k]:
        ct = i + len(memo[k][i])
        difference = a_i[ct - 1] - a_i[i]
    return difference, ct


def calc_base_k_plus_one_index(ct: int) -> int:
    """Calculate the index at which a_i is equal to base[k + 1]"""
    base_k_plus_one_index = (
        a_i.index(base[k + 1], ct) if base[k + 1] in a_i[ct:] else ct
    )
    return base_k_plus_one_index


def add(digits, k, addend):
    """
    adds addend to digit array given in digits
    starting at index k
    """
    for j in range(k, len(digits)):
        s = digits[j] + addend
        if s >= 10:
            quotient, digits[j] = divmod(s, 10)
            addend = addend // 10 + quotient
        else:
            digits[j] = s
            addend = addend // 10

        if addend == 0:
            break

    while addend > 0:
        addend, digit = divmod(addend, 10)
        digits.append(digit)


def solution(n: int = 10**15) -> int:
    """
    returns n-th term of sequence

    >>> solution(10)
    62

    >>> solution(10**6)
    31054319

    >>> solution(10**15)
    73597483551591773
    """

    digits = [1]
    i = 1
    dn = 0
    while True:
        diff, terms_jumped = next_term(digits, 20, i + dn, n)
        dn += terms_jumped
        if dn == n - i:
            break

    a_n = 0
    for j in range(len(digits)):
        a_n += digits[j] * 10**j
    return a_n


if __name__ == "__main__":
    print(f"{solution() = }")
