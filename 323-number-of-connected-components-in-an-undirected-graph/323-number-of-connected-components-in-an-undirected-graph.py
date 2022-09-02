class Solution:
    from collections import defaultdict
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        count = 0
        for node in range(n):
            if not visited[node]:
                self.DFS(node, graph, visited)
                count += 1
        return count
    
    def DFS(self, node, graph, visited):
        
        visited[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.DFS(neighbor, graph, visited)
        