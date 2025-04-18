from collections import deque

class Solution:
    def isBipartite(self, graph):
        
        n = len(graph)
        colors = [-1] * n
    
        def bfs(start):
            queue = deque([start])
            colors[start] = 0  

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if colors[neighbor] == -1:  
                       
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:  
                        return False
            return True
       
        for i in range(n):
            if colors[i] == -1:  
                if not bfs(i):
                    return False

        return True

graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(solution.isBipartite(graph))  
