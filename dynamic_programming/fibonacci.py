"""
This is a pure Python implementation of Dynamic Programming solution to the fibonacci
sequence problem.
"""
from typing import Optional, Tuple


from typing import Optional, Tuple


class Fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]

    def get(self, index: int) -> list:
        """
        Get the Fibonacci number of `index`. If the number does not exist,
        calculate all missing numbers leading up to the number of `index`.

        >>> Fibonacci().get(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> Fibonacci().get(5)
        [0, 1, 1, 2, 3]
        """
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


def main() -> None:
    """
    Main function to interactively calculate and print Fibonacci numbers.
    """
    print(
        "Fibonacci Series Using Dynamic Programming\nEnter the index "
        "of the Fibonacci number you want to calculate in the prompt below. "
        "(To exit enter exit or Ctrl-C)\n"
    )

    fibonacci = Fibonacci()

    while True:
        user_input, should_exit = get_user_input()

        if should_exit:
            break

        if user_input is not None:
            print_fibonacci(fibonacci, user_input)


if __name__ == "__main__":
    main()



def get_user_input() -> Tuple[Optional[int], bool]:
    """Get input from user and return as integer if valid, otherwise return None."""
    prompt: str = input(">> ")

    if prompt in {"exit", "quit"}:
        return None, True

    try:
        index: int = int(prompt)
        return index, False
    except ValueError:
        print("Enter a number or 'exit'")
        return None, False


def print_fibonacci(fibonacci_obj: "Fibonacci", index: int) -> None:
    """Print the Fibonacci number at the specified index."""
    print(fibonacci_obj.get(index))
