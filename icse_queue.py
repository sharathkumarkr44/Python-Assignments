from typing import Any, Optional


# Do NOT change this file.

class Queue:
    """This class defines all methods that a `Queue` should implement."""

    def enqueue(self, item: Any) -> bool:
        """Adds `item` to the end of the queue. Return `True` for success."""
        raise NotImplementedError()

    def dequeue(self) -> Optional[Any]:
        """Removes and returns the front element from the queue (or `None` if the queue is empty)."""
        raise NotImplementedError()

    def is_empty(self) -> bool:
        """Returns `True` if the queue contains no elements, `False` otherwise."""
        raise NotImplementedError()