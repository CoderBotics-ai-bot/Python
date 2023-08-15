from math import factorial

"""
https://en.wikipedia.org/wiki/Automatic_differentiation#Automatic_differentiation_using_dual_numbers
https://blog.jliszka.org/2013/10/24/exact-numeric-nth-derivatives.html

Note this only works for basic functions, f(x) where the power of x is positive.
"""








class Dual:
    def __init__(self, real, rank):
        self.real = real
        if isinstance(rank, int):
            self.duals = [1] * rank
        else:
            self.duals = rank

    def __repr__(self):
        return (
            f"{self.real}+"
            f"{'+'.join(str(dual)+'E'+str(n+1)for n,dual in enumerate(self.duals))}"
        )

    def reduce(self):
        cur = self.duals.copy()
        while cur[-1] == 0:
            cur.pop(-1)
        return Dual(self.real, cur)

    def __add__(self, other: "Dual") -> "Dual":
        """
        Overloads the addition operation for instances of the Dual class.
        If the other operand is not a Dual instance, it is assumed to be of a numerical type
        and only used for the real part calculation, while the existing dual numbers are retained.

        Ensures the operand's dual parts are the same length before adding.

        Args:
            other (Dual): The other operand which may be a `Dual` instance or a numerical type.

        Returns:
            Dual: A new Dual instance with the summed real and dual numbers.
        """
        real_total = self.real + (other.real if isinstance(other, Dual) else other)
        duals_total = (
            self._combine_duals(other) if isinstance(other, Dual) else self.duals
        )

        return Dual(real_total, duals_total)

    def __sub__(self, other):
        return self + other * -1

    def _combine_duals(self, other: "Dual") -> list:
        """
        Combines the dual parts of `self` and `other` into a new list. Fills in gaps
        with 1s to make both lists of dual numbers the same length before combining.

        Args:
            other (Dual): The other operand which is a `Dual` instance.

        Returns:
            list: A new list of dual numbers.
        """
        s_dual, o_dual = self._level_duals(other)

        return [s + o for s, o in zip(s_dual, o_dual)]

    def __mul__(self, other: "Dual") -> "Dual":
        """
        Multiply a Dual by another Dual or a real number.

        Args:
            other (Dual or int or float): The Dual object or real number to multiply with.

        Returns:
            Dual: The result of the multiplication.

        Raises:
            TypeError: If other is not a Dual object or a real number.
        """
        if not isinstance(other, Dual):
            return self.multiply_with_real(other)

        new_duals = self.initialize_new_duals(other)
        self.add_duales(self, other, new_duals)
        self.add_duales(other, self, new_duals)

        return Dual(self.real * other.real, new_duals)

    def _level_duals(self, other: "Dual") -> tuple:
        """
        Extends the shorter list of dual numbers with 1s until it is the same length as
        the longer list.

        Args:
            other (Dual): The other operand which is a `Dual` instance.

        Returns:
            tuple: The leveled lists of dual numbers.
        """
        s_dual = self.duals.copy()
        o_dual = other.duals.copy()

        len_difference = len(s_dual) - len(o_dual)
        if len_difference > 0:
            o_dual.extend([1] * len_difference)
        elif len_difference < 0:
            s_dual.extend([1] * abs(len_difference))

        return s_dual, o_dual

    def multiply_with_real(self, other: float) -> "Dual":
        return Dual(self.real * other, [dual * other for dual in self.duals])

    @staticmethod
    def initialize_new_duals(other: "Dual") -> list:
        return [0] * (len(self.duals) + len(other.duals) + 1)

    @staticmethod
    def add_duales(first: "Dual", second: "Dual", new_duals: list) -> None:
        for i in range(len(first.duals)):
            new_duals[i] += first.duals[i] * second.real

    def __truediv__(self, other):
        if not isinstance(other, Dual):
            new_duals = []
            for i in self.duals:
                new_duals.append(i / other)
            return Dual(self.real / other, new_duals)
        raise ValueError

    def __floordiv__(self, other):
        if not isinstance(other, Dual):
            new_duals = []
            for i in self.duals:
                new_duals.append(i // other)
            return Dual(self.real // other, new_duals)
        raise ValueError

    def __pow__(self, n):
        if n < 0 or isinstance(n, float):
            raise ValueError("power must be a positive integer")
        if n == 0:
            return 1
        if n == 1:
            return self
        x = self
        for _ in range(n - 1):
            x *= self
        return x


def differentiate(func, position, order):
    """
    >>> differentiate(lambda x: x**2, 2, 2)
    2
    >>> differentiate(lambda x: x**2 * x**4, 9, 2)
    196830
    >>> differentiate(lambda y: 0.5 * (y + 3) ** 6, 3.5, 4)
    7605.0
    >>> differentiate(lambda y: y ** 2, 4, 3)
    0
    >>> differentiate(8, 8, 8)
    Traceback (most recent call last):
        ...
    ValueError: differentiate() requires a function as input for func
    >>> differentiate(lambda x: x **2, "", 1)
    Traceback (most recent call last):
        ...
    ValueError: differentiate() requires a float as input for position
    >>> differentiate(lambda x: x**2, 3, "")
    Traceback (most recent call last):
        ...
    ValueError: differentiate() requires an int as input for order
    """
    if not callable(func):
        raise ValueError("differentiate() requires a function as input for func")
    if not isinstance(position, (float, int)):
        raise ValueError("differentiate() requires a float as input for position")
    if not isinstance(order, int):
        raise ValueError("differentiate() requires an int as input for order")
    d = Dual(position, 1)
    result = func(d)
    if order == 0:
        return result.real
    return result.duals[order - 1] * factorial(order)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    def f(y):
        return y**2 * y**4

    print(differentiate(f, 9, 2))
