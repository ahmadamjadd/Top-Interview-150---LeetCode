from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        ans = []
        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                ans.append(i)
        while q:
            node = q.popleft()
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
                    ans.append(neighbour)
        if len(ans) == numCourses:
            return ans
        else:
            return []



        
