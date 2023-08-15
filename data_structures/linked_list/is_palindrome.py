from typing import Optional


def is_palindrome(head: Optional[Node]) -> bool:
    """
    Check if a singly linked list is a palindrome.
    Args:
    head (Optional[Node]): The head node of the linked list.
    Returns:
    bool: True if the linked list is a palindrome, False otherwise.
    Side Effects:
    The original linked list will be modified. The second half will be reversed.
    """
    if not head:
        return True
    middle_node = get_middle_node(head)
    second_list = reverse_linked_list(middle_node.next)
    middle_node.next = None
    return compare_linked_list(head, second_list)


def is_palindrome_stack(head: Optional[Node]) -> bool:
    """Check if a singly linked list is a palindrome using a stack."""

    if not head or not head.next:
        return True

    middle_node = get_middle_node(head)
    stack = populate_stack(middle_node)
    return compare_stack_linked_list(stack, head)



def populate_stack(node: Optional[Node]) -> list:
    """
    Populate a stack with the values of linked list nodes.
    Args:
        node (Optional[Node]): The start node of the linked list.
    Returns:
        list: A stack populated with node values.
    """
    stack = []
    while node:
        stack.append(node.val)
        node = node.next
    return stack


def compare_stack_linked_list(stack: list, head: Optional[Node]) -> bool:
    """
    Compare the values in a stack with the values in a linked list.
    Args:
        stack (list): A stack populated with node values.
        head (Optional[Node]): The head of the linked list.
    Returns:
        bool: True if the stack and linked list contain the same values, False otherwise.
    """
    while stack:
        if stack.pop() != head.val:
            return False
        head = head.next
    return True

def get_middle_node(head: Node) -> Node:
    """
    Function to get the middle of the linked list.
    """
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse_linked_list(head: Node) -> Node:
    """
    Function to reverse a linked list.
    """
    node = None
    while head:
        nxt = head.next
        head.next = node
        node = head
        head = nxt
    return node


def compare_linked_list(head1: Node, head2: Node) -> bool:
    """
    Function to compare two linked lists.
    """
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True


def is_palindrome_dict(head):
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d:
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True
