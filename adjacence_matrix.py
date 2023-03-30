from typing import List


def in_degree(k: int, m: List[List[int]]) -> int:
    """Returns the number of nodes that directly connect to `k`."""
    count = 0
    for i in range(len(m[k])):
        if (m[i][k] == 1):
            count += 1
    return count


def out_degree(k: int, m: List[List[int]]) -> int:
    """Returns the number of nodes that `k` directly connects to."""
    count = 0
    for i in range(len(m[k])):
        if (m[k][i] == 1):
            count += 1
    return count


def adjacent(k: int, m: List[List[int]]) -> List[int]:
    """Returns the nodes that `k` directly connects to."""
    out = []
    for i in range(len(m[k])):
        if (m[k][i] == 1):
            out.append(i)
    return out


def has_triangle(m: List[List[int]]) -> bool:
    """Returns `True` if and only if m has a cycle of length 3."""
    nodes = len(m)
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                if i != j and i != k and j != k and m[i][j] and m[j][k] and m[k][i]:
                    return True
    return False