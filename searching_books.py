def search_linear(a: list[str], item: str) -> int | None:
    """Searches the list for item linearly. Returns the position of item."""
    for i in range(len(a)):
        if a[i] == item:
            return i
    return None


def search_binary(a: list[str], item: str) -> int | None:
    """Searches the list for item binary. Returns the position of item."""
    def binsearch(a: list[str], x: str, low: int, high: int) -> int | None:
        if high < low:
            return None
        m = (low + high) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            return binsearch(a, x, m + 1, high)
        else:
            return binsearch(a, x, low, m - 1)   
    return binsearch(a, item, 0, len(a) - 1)
    

def search_linear_cmp_count(a: list[str], item: str) -> int:
    count = 0
    for i in range(len(a)):
        count += 1
        if a[i] == item:
            return count
    return count


count = 0


def search_binary_cmp_count(a: list[str], item: str) -> int:
    """Searches the list for item linearly. Returns the number of comparisions needed."""
    def binsearch(a: list[str], x: str, low: int, high: int) -> int:
        global count
        count += 1
        if high < low:
            return count
        m = (low + high) // 2
        if a[m] == x:
            return count
        elif a[m] < x:
            return binsearch(a, x, m + 1, high)
        else:
            return binsearch(a, x, low, m - 1)

    return binsearch(a, item, 0, len(a) - 1)


if __name__ == "__main__":
    books = ["The Immortals of Meluha", 
             "Scion of Ikshvaku", 
             "The 3 Mistakes of My Life", 
             "Half Girlfriend", 
             "Do Epic shit", 
             "The power of your subconcious mind"]
    books.sort()
    print(search_linear(books, "The 3 Mistakes of My Life"))
    print(books)
    print(search_binary(books, "The 3 Mistakes of My Life"))
    linear_cmp_count = search_linear_cmp_count(books, "The 3 Mistakes of My Life")
    binary_cmp_count = search_binary_cmp_count(books, "The 3 Mistakes of My Life")
    print("Linear comparision count is: ", linear_cmp_count)
    print("Binary comparision count is: ", binary_cmp_count)