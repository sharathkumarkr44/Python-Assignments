class DoublyLinkedNode:
    def __init__(
            self,
            item: int = None,
            prev: "DoublyLinkedNode | None" = None,
            next: "DoublyLinkedNode | None" = None
    ) -> None:
        self._item = item
        self._prev = prev
        self._next = next

    def get_item(self):
        return self._item

    def get_next(self):
        return self._next

    def get_prev(self):
        return self._prev

    def set_next(self, new_next):
        self._next = new_next

    def set_prev(self, new_prev):
        self._prev = new_prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = DoublyLinkedNode()
        self._tail = DoublyLinkedNode(prev=self._head)
        self._head.set_next(self._tail)
        self._size = 0

    def __len__(self) -> int:
        count = 0
        current_node = self._head
        while current_node._item is not None:
            count += 1
            current_node = current_node._next
        return count

    def is_empty(self) -> bool:
        if self._head._item is None:
            return True
        return False

    def add_first(self, item: int) -> None:
        new_node = DoublyLinkedNode(item=item,
                                    next=self._head,
                                    prev=None)
        if self._head is not None:
            self._head.set_prev(new_node)

        self._head = new_node
        self._size += 1

    def get_first(self) -> int | None:
        if self.is_empty():
            return None
        else:
            return self._head.get_item()

    def remove_first(self) -> int | None:
        if self.is_empty():
            return None
        out = self._head.get_item()
        self._head = self._head.get_next()
        self._size -= 1
        if self.is_empty():
            tail = None
        return out

    def add_last(self, item: int) -> None:
        new_node = DoublyLinkedNode(item)
        new_node.next = None
        if self._head is None:
            new_node._prev = None
            self._head = new_node
            return

        first_node = self._head
        while first_node.get_next():
            first_node = first_node.get_next()
        first_node.set_next(new_node)
        new_node._prev = first_node

    def get_last(self) -> int | None:
        if self.is_empty():
            return None
        if self._head.get_next is None:
            self._head = None
            return
        curr = self._head
        while curr.get_next() is not None:
            curr = curr.get_next()
        return curr.get_item()

    def remove_last(self) -> int | None:
        if self.is_empty():
            return None
        if self._head.get_next is None:
            self._head = None
            return
        curr = self._head
        while curr.get_next() is not None:
            curr = curr.get_next()

        curr._prev._next = None

    def transverse(self):
        node = self._head
        while node is not None:
            print(node._item)
            node = node._next


if __name__ == "__main__":
    double_list = DoublyLinkedList()
    double_list.add_last(6)
    double_list.add_last(7)
    double_list.add_last(8)
    double_list.add_last(9)
    double_list.add_last(10)
    double_list.transverse()

print(double_list.is_empty())
pass