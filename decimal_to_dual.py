def transform_to_dual(n: int) -> str:
    """Transforms a given decimal number to it's dual representation."""
    q = 1
    base2 = "" 
    while (q > 0):
        r = n % 2
        q = n // 2
        base2 = str(r) + base2
        n = q
    return base2


if __name__ == "__main__":
    print(transform_to_dual(6))
    pass