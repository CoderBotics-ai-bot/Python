from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class Stack(Generic[T]):
    """A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit: int = 10):
        self.stack: list[T] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data: T) -> None:
        """Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self) -> T:
        """
        Pop an element off of the top of the stack.

        >>> Stack().pop()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def peek(self) -> T:
        """
        Peek at the top-most element of the stack.

        >>> Stack().pop()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if a stack is empty."""
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        """Return the size of the stack."""
        return len(self.stack)

    def __contains__(self, item: T) -> bool:
        """Check if item is in stack"""
        return item in self.stack


def test_stack() -> None:
    """
    Conducts a series of tests on the functionality of the Stack
    through well defined helper methods.

    Raises:
        AssertionError: if the operations on the Stack do not behave as
                        expected, based on the specified conditions.
    """
    stack: Stack[int] = Stack(10)

    assert_stack_empty(stack)

    try:
        _ = stack.pop()
    except StackUnderflowError:
        pass
    try:
        _ = stack.peek()
    except StackUnderflowError:
        pass

    assert_stack_operational(stack)

    assert_stack_overflow(stack, 200)

    assert not stack.is_empty()
    assert stack.size() == 10
    assert 5 in stack
    assert 55 not in stack


if __name__ == "__main__":
    test_stack()

def assert_stack_empty(stack: Stack[int]) -> None:
    """
    Validates the behaviour of the Stack when it does not contain any elements.

    Args:
        stack: the Stack object to be validated.

    Raises:
        AssertionError: if the operations on the Stack do not behave as expected,
                        based on the specified conditions.
    """
    assert not bool(stack)
    assert stack.is_empty()
    assert not stack.is_full()
    assert str(stack) == "[]"


def assert_stack_overflow(stack: Stack[int], value: int) -> None:
    """
    Validates the behaviour of the Stack when it is full and an attempt is made
    to add an element.

    Args:
        stack: the Stack object to be validated.
        value: the value to push onto the stack

    Raises:
        AssertionError: if the operations on the Stack do not behave as expected,
                        based on the specified conditions.
    """
    try:
        stack.push(value)
        raise AssertionError  # This should not happen
    except StackOverflowError:
        assert True  # This should happen


def assert_stack_operational(stack: Stack[int], num_stack_elements: int = 10) -> None:
    """
    Validates the behaviour of the Stack when it is being used normally
    (inserting and removing elements, checking its status).

    Args:
        stack: the Stack object to be validated.
        num_stack_elements: the number of elements to add to the stack

    Raises:
        AssertionError: if the operations on the Stack do not behave as expected,
                        based on the specified conditions.
    """
    for i in range(num_stack_elements):
        assert stack.size() == i
        stack.push(i)

    assert bool(stack)
    assert not stack.is_empty()
    assert stack.is_full()
    assert str(stack) == str(list(range(num_stack_elements)))
    assert stack.pop() == num_stack_elements - 1
    assert stack.peek() == num_stack_elements - 2

    stack.push(num_stack_elements * 10)
    assert str(stack) == str(
        list(range(num_stack_elements - 1)) + [num_stack_elements * 10]
    )
