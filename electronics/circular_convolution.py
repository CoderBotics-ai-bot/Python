# https://en.wikipedia.org/wiki/Circular_convolution

"""
Circular convolution, also known as cyclic convolution,
is a special case of periodic convolution, which is the convolution of two
periodic functions that have the same period. Periodic convolution arises,
for example, in the context of the discrete-time Fourier transform (DTFT).
In particular, the DTFT of the product of two discrete sequences is the periodic
convolution of the DTFTs of the individual sequences. And each DTFT is a periodic
summation of a continuous Fourier transform function.

Source: https://en.wikipedia.org/wiki/Circular_convolution
"""

import doctest
from collections import deque

import numpy as np








class CircularConvolution:

    def __init__(self) -> None:
        """
        First signal and second signal are stored as 1-D array
        """

        self.first_signal = [2, 1, 2, -1]
        self.second_signal = [1, 2, 3, 4]

    def circular_convolution(
        self, sequence1: np.ndarray, sequence2: np.ndarray
    ) -> np.ndarray:
        """
        The function performs a circular convolution on the two provided sequences.
        Args:
            sequence1: The first sequence in the convolution operation.
            sequence2: The second sequence in the convolution operation.
        Returns:
            The result of the circular convolution operation.
        Raises:
            ValueError: If the two sequences are not of the same length.
        """
        self._validate_sequences(sequence1, sequence2)

        sequence1_deque = deque(sequence1)
        sequence2_deque = deque(sequence2[::-1])

        return self._perform_convolution(sequence1_deque, sequence2_deque)

    @staticmethod
    def _validate_sequences(sequence1: np.ndarray, sequence2: np.ndarray):
        if len(sequence1) != len(sequence2):
            raise ValueError("The two sequences must be of the same length.")

    @staticmethod
    def _perform_convolution(
        sequence1_deque: deque, sequence2_deque: deque
    ) -> np.ndarray:
        convolution_result = []

        for _ in range(len(sequence1_deque)):
            convolution_result.append(
                sum([x * y for x, y in zip(sequence1_deque, sequence2_deque)])
            )
            sequence1_deque.rotate(1)

        return np.array(convolution_result)


if __name__ == "__main__":
    doctest.testmod()
