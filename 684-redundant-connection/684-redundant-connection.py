from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        for u, v in edges:
            self.visited = [False] * (len(edges) + 1)
            if u in self.graph and v in self.graph and self.DFS(u, v):
                return [u, v]
            self.graph[u].append(v)
            self.graph[v].append(u)
    def DFS(self, u, v):
        if not self.visited[u]:
            self.visited[u] = True
            if u == v:
                return True
            for neighbour in self.graph[u]:
                if self.DFS(neighbour, v):
                    return True
        return False
    