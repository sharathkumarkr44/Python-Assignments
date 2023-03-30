"""
Solution for part 2.
# TODO
"""

number_recursive_calls = 0
number_iterations = 0


def fib1(n: int) -> int:
    """Calculates the `n`th fibonacci number recursively."""
    global number_recursive_calls
    number_recursive_calls += 1
    if n == 0 or n == 1:
        return 1
    else:            
        return fib1(n - 2) + fib1(n - 1)


def fib2(n: int) -> int:
    """Calculates the `n`th fibonacci number iteratively."""
    global number_iterations
    if n == 0 or n == 1:
        return 1
    else: 
        a = 0
        b = 1
        count = 0
        for i in range(n):
            count += 1
            c = a + b
            a = b
            b = c
            number_iterations += 1
        return c


if __name__ == "__main__":
    print(fib1(7))
#   for i in range(16):
#       print(fib1(i))
    print(fib2(7))
    print("No. of recursion calls: ", number_recursive_calls - 1)
    print("No. of iterations : ", number_iterations)