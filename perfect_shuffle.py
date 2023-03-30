def interleave(a: list[int], b: list[int]) -> list[int]:
    """
    Returns a new array with elements consecutively taken from array `a` and
    `b`.
    """
    result = []
    length = len(a)
    for i in range(length):        
        result.append(a[i])
        result.append(b[i])
    return result


def perfect_shuffle(a: list[int]) -> list[int]:
    """Returns a new array that is perfectly shuffled once."""
    half = len(a) // 2
    a_h1 = a[:half]
    a_h2 = a[half:]
    return interleave(a_h1, a_h2)


def shuffle_number(a: int) -> int:
    """Returns the number of perfect shuffles needed to get to the same array."""
    import random
    if a > 0:
        rand_list = []
        for i in range(a):            
            rand_num = random.randint(1, 100)
            rand_list.append(rand_num)
        shuffle_list = perfect_shuffle(rand_list)
        count = 1
        while (shuffle_list != rand_list):
            shuffle_list = perfect_shuffle(shuffle_list)
#           print(shuffle_list)
            count += 1
    return count


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [50, 100, 1, 44, 88, 69, 98, 2]
    print(interleave(a, b))
    print(perfect_shuffle(c))
    print(shuffle_number(52))