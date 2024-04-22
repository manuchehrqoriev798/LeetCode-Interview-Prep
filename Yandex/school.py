import sys
import heapq

MAX_N = 100
INFINITY_VAL = 1e18

def dijkstra(start, graph, numNodes):
    dist = [INFINITY_VAL]*numNodes
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        v = heapq.heappop(queue)[1]
        for w, cost in graph[v]:
            if dist[v] + cost < dist[w]:
                dist[w] = dist[v] + cost
                heapq.heappush(queue, (dist[w], w))
    return dist

def solve():
    numNodes, numEdges = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(numEdges):
        u, v, t = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        edges.append((u, v, t))
    numQueries = int(sys.stdin.readline())
    queries = []
    for _ in range(numQueries):
        u, v, t, c = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        queries.append((u, v, t, c))
    numConditions = int(sys.stdin.readline())
    conditions = []
    for _ in range(numConditions):
        a, b, t = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        conditions.append((a, b, t))
    low, high = 0, 1e9
    answer = -1
    while low <= high:
        mid = (low + high) // 2
        graph = [[] for _ in range(numNodes)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        for u, v, t, c in queries:
            if c <= mid:
                graph[u].append((v, t))
                graph[v].append((u, t))
        dist = [dijkstra(i, graph, numNodes) for i in range(numNodes)]
        if all(dist[a][b] <= t for a, b, t in conditions):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    validIds = []
    for i in range(numQueries):
        if queries[i][3] <= answer:
            validIds.append(i + 1)
    # print(answer)
    if answer != -1:
        print(len(validIds))
        for id in validIds:
            print(id, end=" ")

if __name__ == "__main__":
    solve()








# import sys
# import math

# max_num = 100
# infinity = 1e18

# def is_feasible(maxCost, numNodes, numQueries, numConditions, distances, queryU, queryV, queryTime, queryCost, conditionA, conditionB, conditionTime):
#     f = [[0]*max_num for _ in range(max_num)]
#     for i in range(numNodes):
#         for j in range(numNodes):
#             f[i][j] = distances[i][j]
#     for i in range(numQueries):
#         if queryCost[i] <= maxCost:
#             f[queryU[i]][queryV[i]] = queryTime[i]
#             f[queryV[i]][queryU[i]] = queryTime[i]
#     for t in range(numNodes):
#         for i in range(numNodes):
#             for j in range(numNodes):
#                 f[i][j] = min(f[i][j], f[i][t] + f[t][j])
#     for i in range(numConditions):
#         if f[conditionA[i]][conditionB[i]] > conditionTime[i]:
#             return False
#     return True

# def main():
#     numNodes, numEdges = map(int, sys.stdin.readline().split())
#     distances = [[infinity]*max_num for _ in range(max_num)]
#     for i in range(numEdges):
#         u, v, t = map(int, sys.stdin.readline().split())
#         u -= 1
#         v -= 1
#         distances[u][v] = distances[v][u] = t
#     numQueries = int(sys.stdin.readline())
#     queryU, queryV, queryTime, queryCost = [], [], [], []
#     for _ in range(numQueries):
#         u, v, t, c = map(int, sys.stdin.readline().split())
#         queryU.append(u-1)
#         queryV.append(v-1)
#         queryTime.append(t)
#         queryCost.append(c)
#     numConditions = int(sys.stdin.readline())
#     conditionA, conditionB, conditionTime = [], [], []
#     for _ in range(numConditions):
#         a, b, t = map(int, sys.stdin.readline().split())
#         conditionA.append(a-1)
#         conditionB.append(b-1)
#         conditionTime.append(t)
#     low, high = 0, 1e9
#     answer = -1
#     while low <= high:
#         mid = (low + high) // 2
#         if is_feasible(mid, numNodes, numQueries, numConditions, distances, queryU, queryV, queryTime, queryCost, conditionA, conditionB, conditionTime):
#             high = mid - 1
#             answer = mid
#         else:
#             low = mid + 1
#     validIds = []
#     for i in range(numQueries):
#         if queryCost[i] <= answer:
#             validIds.append(i + 1)
#     if answer == -1:
#         print(answer)
#         return
#     print(len(validIds))
#     for id in validIds:
#         print(id, end=" ")

# if __name__ == "__main__":
#     main()





# import sys
# from heapq import *

# INF = 1e18

# def check():
#     node, count1 = map(int, input().split())
#     edge = [list(map(int, input().split())) for _ in range(count1)]
#     count2 = int(input())
#     q = [list(map(int, input().split())) for _ in range(count2)]
#     count3 = int(input())
#     conditions = [list(map(int, input().split())) for _ in range(count3)]

#     dist = [[INF]*node for _ in range(node)]
#     for u, v, t in edge:
#         u -= 1
#         v -= 1
#         dist[u][v] = t
#         dist[v][u] = t

#     for k in range(node):
#         for i in range(node):
#             for j in range(node):
#                 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

#     q.sort(key=lambda x: x[3])
#     for u, v, t, c in q:
#         u -= 1
#         v -= 1
#         if dist[u][v] > t:
#             dist[u][v] = t
#             dist[v][u] = t
#             for i in range(node):
#                 for j in range(node):
#                     dist[i][j] = min(dist[i][j], min(dist[i][u] + dist[v][j] + t, dist[i][v] + dist[u][j] + t))

#     for a, b, t in conditions:
#         a -= 1
#         b -= 1
#         if dist[a][b] > t:
#             print(-1)
#             return

#     print(len(q))
#     for i in range(len(q)):
#         print(i+1, end=' ')
#     print()

# check()
