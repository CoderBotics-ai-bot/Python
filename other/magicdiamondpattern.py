
def floyd(n: int) -> None:
    """
    Prints the upper half of the diamond (pyramid) for a given size.

    This function generates and prints the upper half of a diamond (pyramid)
    shape made up of "*" characters. The diamond is pyramid-shaped, with a
    number of rows equal to the inputted size.

    Each row of the diamond consists of a series of spaces followed by a series
    of "* " (star and space). The number of spaces decreases with each subsequent
    line, while the number of "* " increases, creating a pyramid effect.

    Parameters:
    n (int): The size of the pattern. Determines the number of rows in the upper
             half of the diamond and the number of "* " in the middle row.

    Returns:
    None: This function only prints to the console and does not have a return value.
    """
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))


# Function to print lower half of diamond (pyramid)
def reverse_floyd(n):
    """
        Parameters:
    n : size of pattern
    """
    for i in range(n, 0, -1):
        for _ in range(i, 0, -1):  # printing stars
            print("* ", end="")
        print()
        for _ in range(n - i + 1, 0, -1):  # printing spaces
            print(" ", end="")


# Function to print complete diamond pattern of "*"
def pretty_print(n):
    """
        Parameters:
    n : size of pattern
    """
    if n <= 0:
        print("       ...       ....        nothing printing :(")
        return
    floyd(n)  # upper half
    reverse_floyd(n)  # lower half


if __name__ == "__main__":
    print(r"| /\ | |- |  |-  |--| |\  /| |-")
    print(r"|/  \| |- |_ |_  |__| | \/ | |_")
    K = 1
    while K:
        user_number = int(input("enter the number and , and see the magic : "))
        print()
        pretty_print(user_number)
        K = int(input("press 0 to exit... and 1 to continue..."))

    print("Good Bye...")
