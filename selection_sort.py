"""
1.  An in-place sorting algorithm sorts the elements in place: that is, it needs only O(1) extra space.
An out-of-place sorting algorithm needs extra space to put the elements in as it's sorting them. 
Usually this means O(n) extra space.

3.  AS sorting takes place in each step, at 0% the array is in original state and as the step continues 
till 100% we get a incremental curve stating the values staring from 0th place till 100th place in a 
ascending manner i.e sorted. The animation also portrays the sorting step finally forming a triangle form.

"""


def selection_sort(array: list) -> None:
    """Sorts `array` with selectionsort inplace."""
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if (array[j] < array[min_index]):
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    print(array)
    selection_sort(array)
    print(array)
    assert array == [1, 2, 3, 4, 5]