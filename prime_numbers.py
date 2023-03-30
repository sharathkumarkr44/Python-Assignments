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


if __name__ == '__main__':
    n = int(input('Find the prime number of: '))
    print(is_prime(n))
    print(next_prime(n))