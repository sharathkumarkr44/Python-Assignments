from typing import List
from random import randint
import time


def binary_search(a: List[int], item: int) -> int | None:
    """Searches the list for item with binary search. Returns the position of item."""
    def binsearch(a: list[int], x: int, low: int, high: int) -> int | None:
        if high < low:
            return None
        m = (low + high) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            return binsearch(a, x, m + 1, high)
        else:
            return binsearch(a, x, low, m - 1)   
    return binsearch(a, item, 0, len(a) - 1)


def binary_search_helper(a: List[int], item: int, low: int, high: int) -> int | None:
    raise NotImplementedError()  # TODO: Add implementation


def ternary_search(a: List[int], item: int) -> int | None:
    """Searches the list for item with ternary search. Returns the position of item."""
    def ternSearch(a: list[int], x: int, low: int, high: int) -> int | None:
        if high < low:
            return None
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if (a[mid1] == x):
            return mid1
        if (a[mid2] == x):
            return mid2
        elif (x < a[mid1]):
            return ternSearch(a, x, low, mid1 - 1)
        elif (x > a[mid2]):
            return ternSearch(a, x, mid2 + 1, high)
        else:
            return ternSearch(a, x, mid1 + 1, mid2 - 1)
    return ternSearch(a, item, 0, len(a) - 1)
        
        
def time_binary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    binary_search(arr, item)
    return time.time() - start


def time_ternary_search_in_s(arr: List[int], item: int) -> float:
    start = time.time()
    ternary_search(arr, item)
    return time.time() - start


if __name__ == "__main__":
    # TODO: Test your binary and ternary search implementation here...
    a = [1, 32, 44, 79, 111, 333, 479, 654, 1111, 55000, 89745, 9999998754]
    print(binary_search(a, 333))
    print(ternary_search(a, 333))

    # These constants should be defined here, don't move them!
    MAX_VALUE = 50_000_000
    NUM_ITER = 100_000
    SEARCH_VALUES = [randint(0, MAX_VALUE - 1) for _ in range(NUM_ITER)]
    ARRAY = list(range(MAX_VALUE))
    print(f"Searching {NUM_ITER:_} random values in an array of size {MAX_VALUE:_}")

    time_binary = 0.
    for value in SEARCH_VALUES:
        time_binary += time_binary_search_in_s(ARRAY, value)

    time_ternary = 0.
    for value in SEARCH_VALUES:
        time_ternary += time_ternary_search_in_s(ARRAY, value)

    print(f"Total binary search time:    {time_binary:.9f} s")
    print(f"Total ternary search time:   {time_ternary:.9f} s")
    print(f"Average binary search time:  {time_binary / NUM_ITER:.9f} s")
    print(f"Average ternary search time: {time_ternary / NUM_ITER:.9f} s")

    a = [1, 32, 44, 79, 111, 333, 479, 654, 1111, 55000, 89745, 9999998754]
    print(binary_search(a, 333))
    print(ternary_search(a, 333))