"""
This algorithm compares 2 elements starting from left of the list and the highest element
bubbles out to the right of the list. 
At 0% the list is unsorted.
At 20% highest element of the list is placed at the right corner(sorted)
At 40% second and third highest element is placed at right in the sequence
and this process continues untill every elements are sorted forming the 
triangle from right to left as in graph.
"""


def bubble_sort(array: list) -> None:
    """Sorts `array` with bubblesort inplace."""
    n = len(array)
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    print(array)
    bubble_sort(array)
    print(array)
    assert array == [1, 2, 3, 4, 5]