from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for src, dest in prerequisites:
            adj[src].append(dest)
            indegree[dest] +=1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        processed_nodes = 0
        while q:
            node = q.popleft()
            processed_nodes +=1
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return processed_nodes == numCourses




        
