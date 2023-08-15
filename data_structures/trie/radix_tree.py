"""
A Radix Tree is a data structure that represents a space-optimized
trie (prefix tree) in whicheach node that is the only child is merged
with its parent [https://en.wikipedia.org/wiki/Radix_tree]
"""




class RadixNode:
    def __init__(self, prefix: str = "", is_leaf: bool = False) -> None:
        # Mapping from the first character of the prefix of the node
        self.nodes: dict[str, RadixNode] = {}

        # A node will be a leaf if the tree contains its word
        self.is_leaf = is_leaf

        self.prefix = prefix

    def match(self, word: str) -> tuple[str, str, str]:
        """Compute the common substring of the prefix of the node and a word

        Args:
            word (str): word to compare

        Returns:
            (str, str, str): common substring, remaining prefix, remaining word

        >>> RadixNode("myprefix").match("mystring")
        ('my', 'prefix', 'string')
        """
        x = 0
        for q, w in zip(self.prefix, word):
            if q != w:
                break

            x += 1

        return self.prefix[:x], self.prefix[x:], word[x:]

    def insert_many(self, words: list[str]) -> None:
        """Insert many words in the tree

        Args:
            words (list[str]): list of words

        >>> RadixNode("myprefix").insert_many(["mystring", "hello"])
        """
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        word = word.lower()

        if not self.prefix:
            self.prefix, self.is_leaf = word, True
            return

        i = self._get_common_prefix_index(word)

        if i < len(self.prefix):
            self._handle_partial_match(word, i)
        else:
            self._handle_full_match(word, i)

    def find(self, word: str) -> bool:
        """Returns if the word is on the tree

        Args:
            word (str): word to check

        Returns:
            bool: True if the word appears on the tree

        >>> RadixNode("myprefix").find("mystring")
        False
        """
        incoming_node = self.nodes.get(word[0], None)
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(
                word
            )
            # If there is remaining prefix, the word can't be on the tree
            if remaining_prefix != "":
                return False
            # This applies when the word and the prefix are equal
            elif remaining_word == "":
                return incoming_node.is_leaf
            # We have word remaining so we check the next node
            else:
                return incoming_node.find(remaining_word)

    def _get_common_prefix_index(self, word: str) -> int:
        i = 0
        while i < min(len(word), len(self.prefix)) and word[i] == self.prefix[i]:
            i += 1
        return i

    def _handle_partial_match(self, word: str, i: int) -> None:
        common_prefix = word[:i]
        remaining_prefix_current = self.prefix[i:]
        remaining_prefix_word = word[i:]

        # Create new node for common prefix
        new_node = RadixNode(common_prefix, False)

        # Modify prefixes of the current and next node,
        # also move the next node to be the child of the new common prefix node.
        new_node.children[remaining_prefix_current] = self
        self.prefix = remaining_prefix_current
        self.parent.children[common_prefix] = new_node
        new_node.parent = self.parent
        self.parent = new_node

        # If any remaining part of the word is still left, insert it into the tree using current node.
        if remaining_prefix_word:
            new_node.insert(remaining_prefix_word)

    def _handle_full_match(self, word: str, i: int) -> None:
        if i < len(word):
            remaining_word = word[i:]
            if remaining_word not in self.children:
                self.children[remaining_word] = RadixNode(remaining_word, True)
            else:
                self.children[remaining_word].insert(remaining_word)
        else:
            self.is_leaf = True

    def delete(self, word: str) -> bool:
        """Deletes a word from the tree if it exists

        Args:
            word (str): word to be deleted

        Returns:
            bool: True if the word was found and deleted. False if word is not found

        >>> RadixNode("myprefix").delete("mystring")
        False
        """
        incoming_node = self.nodes.get(word[0], None)
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(
                word
            )
            # If there is remaining prefix, the word can't be on the tree
            if remaining_prefix != "":
                return False
            # We have word remaining so we check the next node
            elif remaining_word != "":
                return incoming_node.delete(remaining_word)
            else:
                # If it is not a leaf, we don't have to delete
                if not incoming_node.is_leaf:
                    return False
                else:
                    # We delete the nodes if no edges go from it
                    if len(incoming_node.nodes) == 0:
                        del self.nodes[word[0]]
                        # We merge the current node with its only child
                        if len(self.nodes) == 1 and not self.is_leaf:
                            merging_node = next(iter(self.nodes.values()))
                            self.is_leaf = merging_node.is_leaf
                            self.prefix += merging_node.prefix
                            self.nodes = merging_node.nodes
                    # If there is more than 1 edge, we just mark it as non-leaf
                    elif len(incoming_node.nodes) > 1:
                        incoming_node.is_leaf = False
                    # If there is 1 edge, we merge it with its child
                    else:
                        merging_node = next(iter(incoming_node.nodes.values()))
                        incoming_node.is_leaf = merging_node.is_leaf
                        incoming_node.prefix += merging_node.prefix
                        incoming_node.nodes = merging_node.nodes

                    return True

    def print_tree(self, height: int = 0) -> None:
        """Print the tree

        Args:
            height (int, optional): Height of the printed node
        """
        if self.prefix != "":
            print("-" * height, self.prefix, "  (leaf)" if self.is_leaf else "")

        for value in self.nodes.values():
            value.print_tree(height + 1)


def test_trie() -> bool:
    words = "banana bananas bandana band apple all beast".split()
    root = RadixNode()
    root.insert_many(words)

    assert all(root.find(word) for word in words)
    assert not root.find("bandanas")
    assert not root.find("apps")
    root.delete("all")
    assert not root.find("all")
    root.delete("banana")
    assert not root.find("banana")
    assert root.find("bananas")

    return True


def pytests() -> None:
    assert test_trie()


def main() -> None:
    """
    >>> pytests()
    """
    root = RadixNode()
    words = "banana bananas bandanas bandana band apple all beast".split()
    root.insert_many(words)

    print("Words:", words)
    print("Tree:")
    root.print_tree()


if __name__ == "__main__":
    main()
