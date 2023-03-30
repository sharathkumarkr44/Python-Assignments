from typing import Any, Optional

# Do NOT change this file


class BinaryTree:
    """The base class for a Binary Tree."""

    def __init__(
        self,
        item: Any,
        left: "Optional[BinaryTree]" = None,
        right: "Optional[BinaryTree]" = None
    ) -> None:
        self._item = item
        self._left = left

        if self._left is not None:
            self._left._parent = left
        self._right = right

        if self._left is not None:
            self._left._parent = self
        self._left = left

        self._parent: "Optional[BinaryTree]" = None

    def is_root(self) -> bool:
        return self._parent is None

    def get_parent(self) -> "Optional[BinaryTree]":
        return self._parent

    def get_left(self) -> "Optional[BinaryTree]":
        return self._left

    def get_right(self) -> "Optional[BinaryTree]":
        return self._right

    def get_item(self) -> Any:
        return self._item

    def get_root(self) -> "Optional[BinaryTree]":
        node: "Optional[BinaryTree]" = self
        while node and not node.is_root():
            node = node.get_parent()
        return node

    def set_left(self, left: "BinaryTree") -> None:
        self._left = left
        self._left._parent = self

    def set_right(self, right: "BinaryTree") -> None:
        self._right = right
        self._right._parent = self
