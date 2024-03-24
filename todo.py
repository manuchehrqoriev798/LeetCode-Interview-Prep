# Motivation is temporarily, have a discipline !
Don't search for the right choice, make the choice right !!!

# You should understand what happens if any line of code will be removed.

I believe that I can do it !





#TODO list:
Yandex Preparation
Open source contribution 






















from collections import defaultdict
from sortedcontainers import SortedSet

N, Q = map(int, input().split())

rooks = set()
free_rows = SortedSet(range(1, N+1))
free_cols = SortedSet(range(1, N+1))

for _ in range(Q):
    query = list(map(str, input().split()))
    command, x, y = query[0], int(query[1]), int(query[2])

    if command == '+':
        rooks.add((x, y))
        if x in free_rows:
            free_rows.remove(x)
        if y in free_cols:
            free_cols.remove(y)
    else:
        rooks.remove((x, y))
        if all(r != x for r, _ in rooks):
            free_rows.add(x)
        if all(c != y for _, c in rooks):
            free_cols.add(y)

    print(max(len(free_rows), len(free_cols)))

























