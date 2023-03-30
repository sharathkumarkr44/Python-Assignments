from typing import Any, Optional

from icse_queue import Queue


class RandomQueue(Queue):
    # TODO: Implement the missing methods.
    def __init__(self) -> None:
        self.__queue: list[Any] = []

    def is_empty(self) -> bool:
        return self.__queue == []

    def enqueue(self, item: Any) -> bool:
        self.__queue = self.__queue + [item]
        return True

    def dequeue(self) -> Optional[Any]:
        """Remove and return one random item from the queue (or `None` if the queue is empty)."""
        if self.__queue == []:
            return None
        else:
            return self.__queue.pop(0)

    def sample(self) -> Optional[Any]:
        """Returns a random element from the queue (or `None` if the queue is empty)."""
        if self.__queue == []:
            return None
        return self.__queue[0]


if __name__ == "__main__":
    Q1 = RandomQueue()
    print(Q1.is_empty())
    print(Q1.enqueue(4))
    print(Q1.enqueue(55))
    print(Q1.enqueue(144))
    print(Q1.dequeue())
    print(Q1.dequeue())
    print(Q1.dequeue())
    print(Q1.dequeue())