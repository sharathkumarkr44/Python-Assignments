def create_random(n: int) -> list[int]:
    """Creates an array with `n` random integers in the range `[5, 99]`"""
    import random
    rand_num_list = []
    for i in range(n):
        rand_num = random.randint(5, 99)
        rand_num_list.append(rand_num)
    return rand_num_list


def to_string(a: list[int]) -> str:
    """Creates a string from an array."""
    str_array = ""
    for i in a:
        str_array += str(i)
    return str_array


def pos_min(a: list[int]) -> int:
    """
    Returns the position of the smallest element in `a`. If it is not unique, it
    returns the position of the first one.
    """
    min_num = min(a)
    index = a.index(min_num)
    return index


def swap(a: list[int]) -> None:
    """Swaps the first and last element in `a`."""
    length = len(a)
    first = a[0]
    last = a[length - 1]
    a[0] = last
    a[length - 1] = first
#   return a


if __name__ == "__main__":
    arr = create_random(5)
    print(arr)
    print(type(arr))
    print("******************************")
    tostr = to_string(arr)
    print(tostr)
    print(type(tostr))
    new = str(arr)
    print(new)
    print(type(new))
    print("******************************")
    print(pos_min(arr))
#   print(swap(arr))