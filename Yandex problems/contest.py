
# It should be 4 because of because there are only 4 uinqe position where player can stay: (0,-1,2,1)
# FLF 0
# LLF -1
# RFF 2
# RRF 1
# RLL 0
# RLR 0


































# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.util.Arrays;
# import java.util.StringTokenizer;

# public class Main {
#     public static void main(String[] args) throws IOException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         StringTokenizer st;

#         int n = Integer.parseInt(br.readLine());
#         int[][] a = new int[n][2];
#         for (int i = 0; i < n; i++) {
#             st = new StringTokenizer(br.readLine());
#             a[i][0] = Integer.parseInt(st.nextToken());
#             a[i][1] = Integer.parseInt(st.nextToken());
#         }

#         Arrays.sort(a, (i, j) -> {
#             if (i[0] == j[0]) {
#                 return Integer.compare(j[1], i[1]);
#             }
#             return Integer.compare(i[0], j[0]);
#         });

#         int mx = 0;
#         int[] vec = new int[n];
#         int size = 0;
#         for (int i = 0; i < n; i++) {
#             int pos = Arrays.binarySearch(vec, 0, size, a[i][1]);
#             if (pos < 0) {
#                 pos = -(pos + 1);
#                 if (pos == size && a[i][1] > mx) {
#                     vec[size++] = a[i][1];
#                 } else {
#                     int sz = size;
#                     for (int k = 0; k < sz - pos; k++) {
#                         size--;
#                     }
#                 }
#             }
#             mx = Math.max(mx, a[i][1]);
#         }

#         System.out.println(size);
#     }
# }















































# import bisect

# n, q = map(int, input().split())

# a = []
# for _ in range(n):
#     a.append(input())

# a.sort()

# for _ in range(q):
#     pos, pr = input().split()
#     pos = int(pos) - 1

#     ins_pos = bisect.bisect_left(a, pr)

#     if ins_pos + pos >= n:
#         print("-1")
#         continue

#     s = a[ins_pos + pos]
#     flg = False
#     j = 0
#     for i in range(min(len(pr), len(s))):
#         if s[i] != pr[j]:
#             print("-1")
#             flg = True
#             break
#         j += 1
#     if flg:
#         continue
#     if j != len(pr):
#         print("-1")
#         continue

#     print(ins_pos + pos + 1)
































# input_string = input()

# words_list = []
# current_word = []
# for char in input_string:
#     if char == ",":
#         if char == ',' and len(current_word) == 0:
#             words_list[-1].append(',')
#         else:
#             current_word.append(',')
#             words_list.append(current_word)
#             current_word = []
#     elif char == ' ':
#         if len(current_word) > 0:
#             words_list.append(current_word)
#             current_word = []
#     else:
#         current_word.append(char)

# if len(current_word) > 0:
#     words_list.append(current_word)

# max_length = 0

# for i in range(len(words_list)):
#     size = len(words_list[i])
#     if words_list[i][-1] == ',':
#         size -= 1

#     max_length = max(max_length, size)
#     words_list[i] = "".join(words_list[i])

# line_length = 3 * max_length

# formatted_lines = []

# words_list.reverse()

# while len(words_list) > 0:
#     current_line = []
#     remaining_length = line_length
#     while len(words_list) > 0 and 0 < remaining_length and remaining_length >= len(words_list[-1]):
#         temp = words_list.pop()
#         current_line.append(temp)
#         remaining_length -= len(temp)

#         if len(words_list) > 0 and remaining_length >= (len(words_list[-1]) + 1):
#             remaining_length -= 1
#         else:
#             break
#     formatted_lines.append(current_line)

# for line in formatted_lines:
#     print(" ".join(line))
