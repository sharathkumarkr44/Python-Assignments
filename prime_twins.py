def is_prime(n: int) -> bool:
    """Returns `True`, if and only if `n` is prime."""
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True


def next_prime(n: int) -> int:
    """Returns the next prime number that is bigger or equal to `n`."""
    prime = is_prime(n)
    if prime is False:
        while (True):
            nxt_prime = is_prime(n)
            if (nxt_prime):
                return n
            n += 1
    else:
        return n
       

def prime_twins(n: int) -> list[tuple[int, int]]:
    """Returns the first n prime twins."""
    count = 0
    i = 2
    twin_tuple = []
    while (count < n):
        p = next_prime(i)
        q = next_prime(p + 1)
        if (q == p + 2):
            twin_tuple.append((p, q))
            count += 1
        i = q
    return twin_tuple


def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    """Returns the first n prime triplets."""
    count = 0
    i = 2
    twin_tuple = []
    while (count < n):
        p = next_prime(i)
        q = next_prime(p + 1)
        r = next_prime(q + 1)
        if ((q == p + 2 or q == p + 4) and r == p + 6):
            twin_tuple.append((p, q, r))
            count += 1
        i = q
    return twin_tuple


if __name__ == "__main__":
    print(prime_twins(11))
    assert prime_twins(2) == [(3, 5), (5, 7)]
    print(prime_triplets(5))
