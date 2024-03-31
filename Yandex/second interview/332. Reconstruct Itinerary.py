from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph for each airport and keep list of airport reachable from it
        graph = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            graph[src].append(dst)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]