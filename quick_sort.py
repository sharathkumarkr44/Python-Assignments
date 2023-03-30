"""
2.  

3.  Best case occurs generally when the list is in completely random manner. complexity : O(n logn)
    Worst case occurs when the array is already sorted either in ascending or descending order.
    complexity : O(n^2)

    Note:- choose 3 random elements from list and take median as the pivot to reduce worst case scenario. 

"""


def quick_sort(array: list) -> None:
    """Sorts `array` with quick-sort in-place."""
    def partition(array: list, low: int, high: int) -> int:
        # Choose the rightmost element as pivot
        pivot = array[high]
        # Pointer for greater element
        i = low - 1
        # Traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])
    
        # Swap the pivot element with 
        # the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
    
        # Return the position from where partition is done
        return i + 1
   
    def _quick_sort(array: list, low: int, high: int) -> None:
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = partition(array, low, high)
    
            # Recursive call on the left of pivot
            _quick_sort(array, low, pi - 1)
    
            # Recursive call on the right of pivot
            _quick_sort(array, pi + 1, high)
        
    _quick_sort(array, 0, len(array) - 1)


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    print(array)
    quick_sort(array)
    print(array)
    assert array == [1, 2, 3, 4, 5]