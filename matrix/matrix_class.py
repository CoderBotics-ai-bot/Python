# An OOP approach to representing and manipulating matrices

from __future__ import annotations


from typing import List, Union
































































































































































































































































































































































































































































































































class Matrix:

    def __init__(self, elements: List[List[Union[int, float]]]):
        """Initializes a Matrix object"""
        self._validate_input(elements)
        self.rows = [Row(row) for row in elements]
        self.columns = self._get_columns()

    # MATRIX INFORMATION
    def columns(self) -> list[list[int]]:
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    def _validate_input(self, elements: List[List[Union[int, float]]]):
        """Validates the input for the Matrix constructor"""
        if not elements or not all(elements):
            raise ValueError("Matrix cannot be empty")

        num_columns = len(elements[0])
        if not all(len(row) == num_columns for row in elements):
            raise ValueError("All rows must have the same number of elements")

    def _get_columns(self) -> List[List[Union[int, float]]]:
        """Returns the columns of the matrix"""
        return [[row[idx] for row in self.rows] for idx in range(len(self.rows[0]))]

    @property
    def num_rows(self) -> int:
        return len(self.rows)

    @property
    def num_columns(self) -> int:
        return len(self.rows[0])

    @property
    def order(self) -> tuple[int, int]:
        return self.num_rows, self.num_columns

    @staticmethod
    def identity(elements: Union[List[int], List[str]]) -> Union[List[int], List[str]]:
        return elements

    def determinant(self, matrix: List[List[Union[int, float]]]) -> Union[int, float]:
        """
        Calculate the determinant of a matrix.

        The determinant calculation is done using the method of minors of a matrix.

        :param matrix: list[list[int/float]] : a 2D list representing the matrix
        :return: int/float : determinant of the matrix
        """
        total = 0
        size = len(matrix)

        if size == 1:
            return matrix[0][0]

        # define submatrix for focus column
        for focus_col in range(size):
            sign = (-1) ** focus_col

            # call this function again for smaller matrix
            sub_matrix = self.minor(matrix, 0, focus_col)

            # add current result to the total calculation
            total += sign * matrix[0][focus_col] * self.determinant(sub_matrix)

        return total

    def minor(
        self, matrix: List[List[Union[int, float]]], row: int, col: int
    ) -> List[List[Union[int, float]]]:
        """Compute the minor of the matrix after removing specific row and column."""
        return [
            row[:col] + row[col + 1 :] for idx, row in enumerate(matrix) if idx != row
        ]

    def get_minor(
        self, removed_row: int, removed_col: int
    ) -> List[List[Union[int, float]]]:
        """Generates a minor matrix by removing specified row and column.

        Args:
            removed_row (int): The row number to be removed.
            removed_col (int): The column number to be removed.

        Returns:
            List[List[Union[int, float]]]: The minor matrix after the row and the column are removed.
        """
        return self._create_minor_matrix(removed_row, removed_col)

    def _create_minor_matrix(
        self, removed_row: int, removed_col: int
    ) -> List[List[Union[int, float]]]:
        """Creates a minor matrix by removing the specified row and column from the original matrix.

        Args:
            removed_row (int): The row number to be removed.
            removed_col (int): The column number to be removed.

        Returns:
            List[List[Union[int, float]]]: The minor matrix after the row and the column are removed.
        """
        return [
            row[:removed_col] + row[removed_col + 1 :]
            for i, row in enumerate(self.matrix)
            if i != removed_row
        ]

    @property
    def is_square(self) -> bool:
        return self.order[0] == self.order[1]

    def is_invertable(self) -> bool:
        return bool(self.determinant())

    def get_cofactor(self, row: int, column: int) -> int:
        if (row + column) % 2 == 0:
            return self.get_minor(row, column)
        return -1 * self.get_minor(row, column)

    def minors(self) -> Matrix:
        return Matrix(
            [
                [self.get_minor(row, column) for column in range(self.num_columns)]
                for row in range(self.num_rows)
            ]
        )

    def cofactors(self) -> Matrix:
        return Matrix(
            [
                [
                    self.minors().rows[row][column]
                    if (row + column) % 2 == 0
                    else self.minors().rows[row][column] * -1
                    for column in range(self.minors().num_columns)
                ]
                for row in range(self.minors().num_rows)
            ]
        )

    def adjugate(self) -> Matrix:
        values = [
            [self.cofactors().rows[column][row] for column in range(self.num_columns)]
            for row in range(self.num_rows)
        ]
        return Matrix(values)

    def inverse(self) -> Matrix:
        determinant = self.determinant()
        if not determinant:
            raise TypeError("Only matrices with a non-zero determinant have an inverse")
        return self.adjugate() * (1 / determinant)

    def __repr__(self) -> str:
        return str(self.rows)

    def __str__(self) -> str:
        if self.num_rows == 0:
            return "[]"
        if self.num_rows == 1:
            return "[[" + ". ".join(str(self.rows[0])) + "]]"
        return (
            "["
            + "\n ".join(
                [
                    "[" + ". ".join([str(value) for value in row]) + ".]"
                    for row in self.rows
                ]
            )
            + "]"
        )

    # MATRIX MANIPULATION
    def add_row(self, row: list[int], position: int | None = None) -> None:
        type_error = TypeError("Row must be a list containing all ints and/or floats")
        if not isinstance(row, list):
            raise type_error
        for value in row:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(row) != self.num_columns:
            raise ValueError(
                "Row must be equal in length to the other rows in the matrix"
            )
        if position is None:
            self.rows.append(row)
        else:
            self.rows = self.rows[0:position] + [row] + self.rows[position:]

    def add_column(self, column: list[int], position: int | None = None) -> None:
        type_error = TypeError(
            "Column must be a list containing all ints and/or floats"
        )
        if not isinstance(column, list):
            raise type_error
        for value in column:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(column) != self.num_rows:
            raise ValueError(
                "Column must be equal in length to the other columns in the matrix"
            )
        if position is None:
            self.rows = [self.rows[i] + [column[i]] for i in range(self.num_rows)]
        else:
            self.rows = [
                self.rows[i][0:position] + [column[i]] + self.rows[i][position:]
                for i in range(self.num_rows)
            ]

    # MATRIX OPERATIONS
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented
        return self.rows == other.rows

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __neg__(self) -> Matrix:
        return self * -1

    def __add__(self, other: Matrix) -> Matrix:
        if self.order != other.order:
            raise ValueError("Addition requires matrices of the same order")
        return Matrix(
            [
                [self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __sub__(self, other: Matrix) -> Matrix:
        if self.order != other.order:
            raise ValueError("Subtraction requires matrices of the same order")
        return Matrix(
            [
                [self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __mul__(self, other: Matrix | float) -> Matrix:
        if isinstance(other, (int, float)):
            return Matrix(
                [[int(element * other) for element in row] for row in self.rows]
            )
        elif isinstance(other, Matrix):
            if self.num_columns != other.num_rows:
                raise ValueError(
                    "The number of columns in the first matrix must "
                    "be equal to the number of rows in the second"
                )
            return Matrix(
                [
                    [Matrix.dot_product(row, column) for column in other.columns()]
                    for row in self.rows
                ]
            )
        else:
            raise TypeError(
                "A Matrix can only be multiplied by an int, float, or another matrix"
            )

    def __pow__(self, other: int) -> Matrix:
        if not isinstance(other, int):
            raise TypeError("A Matrix can only be raised to the power of an int")
        if not self.is_square:
            raise ValueError("Only square matrices can be raised to a power")
        if other == 0:
            return self.identity()
        if other < 0:
            if self.is_invertable():
                return self.inverse() ** (-other)
            raise ValueError(
                "Only invertable matrices can be raised to a negative power"
            )
        result = self
        for _ in range(other - 1):
            result *= self
        return result

    @classmethod
    def dot_product(cls, row: list[int], column: list[int]) -> int:
        return sum(row[i] * column[i] for i in range(len(row)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
