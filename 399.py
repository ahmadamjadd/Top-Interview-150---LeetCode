from collections import deque
class Solution:
    def bfs(self,graph, startNode, endNode):
        visited = []
        queue = deque([(startNode, 1)])
        visited.append(startNode)
        while queue:
            node, curr_val = queue.popleft()
            if node == endNode:
                return curr_val
            for neighbour, value in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour, curr_val * value))

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        final_ans = []
        graph = {}

        for i, (a, b) in enumerate(equations):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        for query in queries:
            value, neighbour = query
            if value not in graph or neighbour not in graph:
                final_ans.append(-1)
                continue
            final_ans.append(self.bfs(graph, value, neighbour))
        return final_ans
            



            

            

        
