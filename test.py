MAX_N = 100
INFINITY_VAL = 1e18

def is_feasible(max_cost, num_nodes, num_queries, query_u, query_v, query_time, query_cost, condition_a, condition_b, condition_time, distances):
    floyd = [[0]*num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            floyd[i][j] = distances[i][j]
    for i in range(num_queries):
        if query_cost[i] <= max_cost:
            floyd[query_u[i]][query_v[i]] = query_time[i]
            floyd[query_v[i]][query_u[i]] = query_time[i]
    for t in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                floyd[i][j] = min(floyd[i][j], floyd[i][t] + floyd[t][j])
    for i in range(num_conditions):
        if floyd[condition_a[i]][condition_b[i]] > condition_time[i]:
            return False
    return True


    # rest of the code remains same
 def solve():
    num_nodes, num_edges = map(int, input().split())
    distances = [[INFINITY_VAL]*num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        distances[i][i] = 0
    for _ in range(num_edges):
        u, v, t = map(int, input().split())
        u -= 1
        v -= 1
        distances[u][v] = t
        distances[v][u] = t
    num_queries = int(input())
    query_u, query_v, query_time, query_cost = [], [], [], []
    for _ in range(num_queries):
        u, v, t, c = map(int, input().split())
        query_u.append(u-1)
        query_v.append(v-1)
        query_time.append(t)
        query_cost.append(c)
    num_conditions = int(input())
    condition_a, condition_b, condition_time = [], [], []
    for _ in range(num_conditions):
        a, b, t = map(int, input().split())
        condition_a.append(a-1)
        condition_b.append(b-1)
        condition_time.append(t)
    low, high = 0, 1e9
    answer = -1
   while low <= high:
        mid = (low + high) // 2
        if is_feasible(mid, num_nodes, num_queries, query_u, query_v, query_time, query_cost, num_conditions, condition_a, condition_b, condition_time, distances):
            high = mid - 1
            answer = mid
        else:
            low = mid + 1
    valid_ids = [i+1 for i in range(num_queries) if query_cost[i] <= answer]
    if answer == -1:
        print(answer)
        return
    print(len(valid_ids))
    for id in valid_ids:
        print(id, end=" ")

num_tests = 1
for _ in range(num_tests):
    solve()
