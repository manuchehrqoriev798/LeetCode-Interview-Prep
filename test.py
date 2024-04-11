# 1
def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n < 7:
        print("-1")
        return

    cnt = {}
    for i in range(7):
        cnt[a[i]] = cnt.get(a[i], 0) + 1

    ans = -1 if cnt.get(2, 0) > 0 or cnt.get(3, 0) > 0 else cnt.get(5, 0)
    for i in range(7, n):
        cnt[a[i]] = cnt.get(a[i], 0) + 1
        cnt[a[i - 7]] -= 1
        if cnt.get(2, 0) == 0 and cnt.get(3, 0) == 0:
            ans = max(ans, cnt.get(5, 0))

    print(ans)

if __name__ == "__main__":
    tt = 1
    while tt:
        solve()
        tt -= 1





















# 2
def rotate_matrix_90_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - 1 - i] = matrix[i][j]
    return new_matrix

n, m = map(int, input().strip().split())
input_matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    input_matrix.append(row)

output_matrix = rotate_matrix_90_clockwise(input_matrix)

for row in output_matrix:
    print(" ".join(map(str, row)))



























# 3
def print_dirs():
    n = int(input().strip())
    dirs = []
    for _ in range(n):
        dirs.append(input().strip())

    dirs.sort()
    tree = {}
    for dir in dirs:
        parts = dir.split('/')
        node = tree
        for part in parts:
            node = node.setdefault(part, {})

    def print_tree(node, prefix=""):
        for k in sorted(node):
            print(f"{prefix}{k}")
            print_tree(node[k], prefix + "  ")

    print_tree(tree)

print_dirs()




















# 4
def rotate(n, direction, matrix):
    swaps = []
    for i in range(n//2):
        for j in range(i, n-i-1):
            if direction == 'L':
                swaps.append([(i, j), (j, n-i-1)])
                swaps.append([(j, n-i-1), (n-i-1, n-j-1)])
                swaps.append([(n-i-1, n-j-1), (n-j-1, i)])
            else:
                swaps.append([(i, j), (n-j-1, i)])
                swaps.append([(n-j-1, i), (n-i-1, n-j-1)])
                swaps.append([(n-i-1, n-j-1), (j, n-i-1)])
    return swaps

n, direction = input().split()
n = int(n)
matrix = [list(map(int, input().split())) for _ in range(n)]
swaps = rotate(n, direction, matrix)
print(len(swaps))
for swap in swaps:
    print(swap[0][0], swap[0][1], swap[1][0], swap[1][1])
    
    
    
    
    
    
    
    
    























# 5
def solve():
    n = int(input())

    a = [[0] * 3 for _ in range(n + 1)]
    for i in range(1, n + 1):
        s = input()
        for j in range(3):
            if s[j] == 'W':
                a[i][j] = -1
            elif s[j] == 'C':
                a[i][j] = 1

    for i in range(1, n + 1):
        for j in range(3):
            if a[i][j] == -1:
                continue
            val = a[i - 1][j] if a[i - 1][j] != -1 else 0
            if j + 1 < 3 and a[i - 1][j + 1] != -1:
                val = max(val, a[i - 1][j + 1])
            if j - 1 >= 0 and a[i - 1][j - 1] != -1:
                val = max(val, a[i - 1][j - 1])
            a[i][j] += val

    ans = 0
    for i in range(1, n + 1):
        for j in range(3):
            ans = max(ans, a[i][j])

    print(ans)

solve()


n = int(input())
forest = [list(input()) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
dp[0] = [1 if x == 'C' else 0 for x in forest[0]]

for i in range(1, n):
    for j in range(3):
        if forest[i][j] == 'W':
            continue
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        if j < 2:
            dp[i][j] = max(dp[i][j], dp[i-1][j+1])
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if forest[i][j] == 'C':
            dp[i][j] += 1

print(max(dp[-1]))

















































# 6
from collections import deque

def bfs(board, start, end):
    n = len(board)
    dx = [-2, -1, 1, 2, 2, 1, -1, -2, -1, 0, 1, 0, -1, 1, 0, -1]
    dy = [1, 2, 2, 1, -1, -2, -2, -1, 0, 1, 0, -1, 1, 0, -1, 0]
    visited = [[[-1]*2 for _ in range(n)] for _ in range(n)]
    queue = deque([(start[0], start[1], 0, 0)])
    visited[start[0]][start[1]][0] = 0

    while queue:
        x, y, state, dist = queue.popleft()
        if (x, y) == end:
            return dist
        for i in range(8 if state == 0 else 16):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_state = state
                if board[nx][ny] == 'K':
                    new_state = 0
                elif board[nx][ny] == 'G':
                    new_state = 1
                if visited[nx][ny][new_state] == -1:
                    visited[nx][ny][new_state] = dist + 1
                    queue.append((nx, ny, new_state, dist + 1))
    return -1

def solve():
    n = int(input().strip())
    board = []
    start = end = (-1, -1)
    for i in range(n):
        row = list(input().strip())
        board.append(row)
        for j in range(n):
            if row[j] == 'S':
                start = (i, j)
            elif row[j] == 'F':
                end = (i, j)
    print(bfs(board, start, end))

if __name__ == "__main__":
    solve()


















