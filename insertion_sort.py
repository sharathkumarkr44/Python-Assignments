"""
2. Insertion sort makes the element to compare with its neigbour and swap into right place. 
At 0% all items in unsorted order.At 20% the first two elements starts
comparing and smallest element is swappped to the left.
and as the step continues 
till 100% we get a incremental curve stating the values staring from 0th place till 100th place in a 
ascending manner i.e sorted. The animation also portrays the sorting step finally forming a triangle form.
"""


def insertion_sort(array: list) -> None:
    """Sorts `array` with insertionsort inplace."""
    for i in range(1, len(array)):
        j = i
        while (array[j - 1] > array[j] and j > 0):
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    print(array)
    insertion_sort(array)
    print(array)
    assert array == [1, 2, 3, 4, 5]