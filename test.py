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




import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int grade = scanner.nextInt();
        int[] grades = new int[grade];
        for (int i = 0; i < grade; i++) {
            grades[i] = scanner.nextInt();
        }
        scanner.close();

        if (grade < 7) {
            System.out.println("-1");
            return;
        }

        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < 7; i++) {
            count.put(grades[i], count.getOrDefault(grades[i], 0) + 1);
        }

        int res = (count.getOrDefault(2, 0) > 0 || count.getOrDefault(3, 0) > 0) ? -1 : count.getOrDefault(5, 0);
        for (int i = 7; i < grade; i++) {
            count.put(grades[i], count.getOrDefault(grades[i], 0) + 1);
            count.put(grades[i - 7], count.get(grades[i - 7]) - 1);
            if (count.getOrDefault(2, 0) == 0 && count.getOrDefault(3, 0) == 0) {
                res = Math.max(res, count.getOrDefault(5, 0));
            }
        }

        System.out.println(res);
    }
}

















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





import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int rows = scanner.nextInt();
        int cols = scanner.nextInt();
        int[][] initial = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                initial[i][j] = scanner.nextInt();
            }
        }
        scanner.close();

        int[][] finalMatrix = rotate(initial);

        for (int[] row : finalMatrix) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }

    private static int[][] rotate(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] res = new int[cols][rows];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                res[j][rows - 1 - i] = matrix[i][j];
            }
        }
        return res;
    }
}





















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


import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dirCount = scanner.nextInt();
        scanner.nextLine(); 
        List<String> dirs = new ArrayList<>();
        for (int i = 0; i < dirCount; i++) {
            dirs.add(scanner.nextLine());
        }
        scanner.close();

        Collections.sort(dirs);
        Map<String, Map> hashmap = new HashMap<>();
        for (String dir : dirs) {
            String[] parts = dir.split("/");
            Map<String, Map> node = hashmap;
            for (String part : parts) {
                node = node.computeIfAbsent(part, k -> new HashMap<>());
            }
        }

        res(hashmap, "");
    }

    private static void res(Map<String, Map> node, String prefix) {
        List<String> keys = new ArrayList<>(node.keySet());
        Collections.sort(keys);
        for (String key : keys) {
            System.out.println(prefix + key);
            res(node.get(key), prefix + "  ");
        }
    }
}



























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
    
    
    
    
    
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String direction = scanner.next();
        int[][] m = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                m[i][j] = scanner.nextInt();
            }
        }
        scanner.close();

        List<int[][]> changes = rotate(n, direction, m);
        System.out.println(changes.size());
        for (int[][] swap : changes) {
            System.out.println(swap[0][0] + " " + swap[0][1] + " " + swap[1][0] + " " + swap[1][1]);
        }
    }

    private static List<int[][]> rotate(int n, String direction, int[][] m) {
        List<int[][]> changes = new ArrayList<>();
        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - i - 1; j++) {
                if (direction.equals("L")) {
                    changes.add(new int[][]{{i, j}, {j, n - i - 1}});
                    changes.add(new int[][]{{j, n - i - 1}, {n - i - 1, n - j - 1}});
                    changes.add(new int[][]{{n - i - 1, n - j - 1}, {n - j - 1, i}});
                } else {
                    changes.add(new int[][]{{i, j}, {n - j - 1, i}});
                    changes.add(new int[][]{{n - j - 1, i}, {n - i - 1, n - j - 1}});
                    changes.add(new int[][]{{n - i - 1, n - j - 1}, {j, n - i - 1}});
                }
            }
        }
        return changes;
    }
}
  
    
    
    























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










import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        scanner.nextLine(); 
        int[][] points = new int[count + 1][3];
        for (int i = 1; i <= count; i++) {
            String s = scanner.nextLine();
            for (int j = 0; j < 3; j++) {
                if (s.charAt(j) == 'W') {
                    points[i][j] = -1;
                } else if (s.charAt(j) == 'C') {
                    points[i][j] = 1;
                }
            }
        }
        scanner.close();

        for (int i = 1; i <= count; i++) {
            for (int j = 0; j < 3; j++) {
                if (points[i][j] == -1) {
                    continue;
                }
                int val = points[i - 1][j] != -1 ? points[i - 1][j] : 0;
                if (j + 1 < 3 && points[i - 1][j + 1] != -1) {
                    val = Math.max(val, points[i - 1][j + 1]);
                }
                if (j - 1 >= 0 && points[i - 1][j - 1] != -1) {
                    val = Math.max(val, points[i - 1][j - 1]);
                }
                points[i][j] += val;
            }
        }

        int res = 0;
        for (int i = 1; i <= count; i++) {
            for (int j = 0; j < 3; j++) {
                res = Math.max(res, points[i][j]);
            }
        }

        System.out.println(res);
    }
}







































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







import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();  
        char[][] board = new char[n][n];
        int[] start = {-1, -1};
        int[] end = {-1, -1};
        for (int i = 0; i < n; i++) {
            String row = scanner.nextLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = row.charAt(j);
                if (board[i][j] == 'S') {
                    start[0] = i;
                    start[1] = j;
                } else if (board[i][j] == 'F') {
                    end[0] = i;
                    end[1] = j;
                }
            }
        }
        scanner.close();

        System.out.println(bfs(board, start, end));
    }

    private static int bfs(char[][] board, int[] start, int[] end) {
        int n = board.length;
        int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2, -1, 0, 1, 0, -1, 1, 0, -1};
        int[] dy = {1, 2, 2, 1, -1, -2, -2, -1, 0, 1, 0, -1, 1, 0, -1, 0};
        int[][][] visited = new int[n][n][2];
        for (int[][] row : visited) {
            for (int[] cell : row) {
                Arrays.fill(cell, -1);
            }
        }
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{start[0], start[1], 0, 0});
        visited[start[0]][start[1]][0] = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int state = current[2];
            int dist = current[3];
            if (x == end[0] && y == end[1]) {
                return dist;
            }
            for (int i = 0; i < (state == 0 ? 8 : 16); i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    int newState = state;
                    if (board[nx][ny] == 'K') {
                        newState = 0;
                    } else if (board[nx][ny] == 'G') {
                        newState = 1;
                    }
                    if (visited[nx][ny][newState] == -1) {
                        visited[nx][ny][newState] = dist + 1;
                        queue.add(new int[]{nx, ny, newState, dist + 1});
                    }
                }
            }
        }
        return -1;
    }
}














import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();  
        char[][] board = new char[n][n];
        int[] start = {-1, -1};
        int[] end = {-1, -1};
        for (int i = 0; i < n; i++) {
            String row = scanner.nextLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = row.charAt(j);
                if (board[i][j] == 'S') {
                    start[0] = i;
                    start[1] = j;
                } else if (board[i][j] == 'F') {
                    end[0] = i;
                    end[1] = j;
                }
            }
        }
        scanner.close();

        ChessBoard chessBoard = new ChessBoard(board);
        System.out.println(chessBoard.bfs(start, end));
    }
}

class ChessBoard {
    private char[][] board;
    private int[][][] visited;
    private int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2, -1, 0, 1, 0, -1, 1, 0, -1};
    private int[] dy = {1, 2, 2, 1, -1, -2, -2, -1, 0, 1, 0, -1, 1, 0, -1, 0};

    public ChessBoard(char[][] board) {
        this.board = board;
        this.visited = new int[board.length][board.length][2];
        for (int[][] row : visited) {
            for (int[] cell : row) {
                Arrays.fill(cell, -1);
            }
        }
    }

    public int bfs(int[] start, int[] end) {
        int n = board.length;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{start[0], start[1], 0, 0});
        visited[start[0]][start[1]][0] = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int state = current[2];
            int dist = current[3];
            if (x == end[0] && y == end[1]) {
                return dist;
            }
            for (int i = 0; i < (state == 0 ? 8 : 16); i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    int newState = state;
                    if (board[nx][ny] == 'K') {
                        newState = 0;
                    } else if (board[nx][ny] == 'G') {
                        newState = 1;
                    }
                    if (visited[nx][ny][newState] == -1) {
                        visited[nx][ny][newState] = dist + 1;
                        queue.add(new int[]{nx, ny, newState, dist + 1});
                    }
                }
            }
        }
        return -1;
    }
}




























