def makeSchedule(todo):
    graph = {}
    indegree = {}

    # Initialize graph and indegree
    for task, dependencies in todo.items():
        graph[task] = []
        indegree[task] = 0

    # Build the graph and calculate indegree
    for task, dependencies in todo.items():
        for dep_task in dependencies:
            graph[dep_task].append(task)
            indegree[task] += 1

    # Perform topological sorting
    result = []
    queue = [task for task, degree in indegree.items() if degree == 0]

    while queue:
        current_task = queue.pop(0)
        result.append(current_task)

        for dependent_task in graph[current_task]:
            indegree[dependent_task] -= 1
            if indegree[dependent_task] == 0:
                queue.append(dependent_task)

    # Check if all tasks have been processed
    if len(result) != len(todo):
        return []

    return result

# Example usage:
todo1 = {
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
}
print(makeSchedule(todo1))  # Output: [3, 2, 1, 0]

todo2 = {
    0: [],
    1: []
}
print(makeSchedule(todo2))  # Output: [0, 1]

todo3 = {
    0: [1],
    1: [0]
}
print(makeSchedule(todo3))  # Output: []
