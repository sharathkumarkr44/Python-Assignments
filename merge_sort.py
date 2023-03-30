"""
1.  The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm. 
In this algorithm, the array is initially divided into two equal halves and then they are combined 
in a sorted manner.

Stable sorting means that the order of equal elements is the same in the input and output. Merge sort is a stable 
sorting algorithm.

2.  for example of list :- {5, 3, 2, 7, 6, 9, 1, 8, 4, 10}
At first, check if the left index of array is less than the right index, 
if yes then calculate its mid point divide into 2 equal array :- 
{5, 3, 2, 7, 6} and {9, 1, 8, 4, 10}
repeat the process unless the atomic values are achieved
{5, 3, 2}, {7, 6}, {9, 1, 8} and {4, 10}
{5, 3}, {2}, {7}, {6}, {9, 1}, {8}, {4}, {10}
{5}, {3}, {2}, {7}, {6}, {9}, {1}, {8}, {4}, {10}
{3,5}, {2,7}, {6,9}, {1,8}, {4,10}
{2,3,5,7}, {1,6,8,9}, {4,10}
{1,2,3,5,6,7,8,9} , {4,10}
 [1,2,3,4,5,6,7,8,9,10] sorted array!!!


"""


def merge_sort(array: list[int]) -> list[int]:
    """Sorts `array` with merge-sort"""
    def merge(L: list[int], R: list[int]) -> list[int]:
        i, j, n = 0, 0, len(L) + len(R)
        out = [0 for x in range(n)] 
        for k in range(n):
            if i >= len(L): 
                out[k] = R[j] 
                j += 1 
                k += 1
            elif j >= len(R):
                out[k] = L[i] 
                i += 1
                k += 1
            elif L[i] <= R[j]:
                out[k] = L[i] 
                i += 1 
                k += 1 
            else:
                out[k] = R[j] 
                j += 1 
                k += 1
        return out
    
    n = len(array) // 2
    L, R = array[:n], array[n:]
    if len(L) > 1:
        L = merge_sort(L)
    if len(R) > 1:
        R = merge_sort(R)
    out = merge(L, R)
    return out
   
                
if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    print("before sorting", array)
    print("Sorted array: ", merge_sort(array))
    print("original array after sorting: ", array)
#    assert array == [1, 2, 3, 4, 5]