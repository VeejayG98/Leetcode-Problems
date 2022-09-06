from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        no_of_cities = len(isConnected)
        city_graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    city_graph[i].append(j)
                    
        visited = [False] * no_of_cities
        count = 0
        
        for city in range(no_of_cities):
            if not visited[city]:
                self.DFS(city, city_graph, visited)
                count += 1
        return count
    
    def DFS(self, city, city_graph, visited):
        visited[city] = True
        
        for neighbor in city_graph[city]:
            if not visited[neighbor]:
                self.DFS(neighbor, city_graph, visited)
        