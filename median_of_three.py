def median(a: int, b: int, c: int) -> int:
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median        
    raise NotImplementedError()  # TODO: Add implementation


def median2(a: int, b: int, c: int) -> int:
    num_list = [a, b, c]
    num_list.sort()
    median = num_list[1]
    return median
    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    print(median2(9, 4, 77))
    print(median(9, 4, 77))