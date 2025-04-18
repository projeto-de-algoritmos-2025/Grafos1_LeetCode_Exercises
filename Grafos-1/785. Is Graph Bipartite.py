from collections import deque

class Solution:
    def isBipartite(self, graph):
        
        n = len(graph)
        colors = [-1] * n
    
        def bfs(start):
            queue = deque([start])
            colors[start] = 0  # Começamos colorindo o nó de forma arbitrária (0)

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if colors[neighbor] == -1:  # Se o vizinho não foi colorido
                        colors[neighbor] = 1 - colors[node]  # Colorimos o vizinho com a cor oposta
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:  # Se os vizinhos têm a mesma cor
                        return False  # O grafo não é bipartido
            return True
       
        for i in range(n):
            if colors[i] == -1:  # Se o nó ainda não foi colorido
                if not bfs(i):  # Chamamos a BFS para colorir os nós
                    return False

        return True

# Criar uma instância da classe Solution
solution = Solution()

# Testando a função isBipartite
graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(solution.isBipartite(graph))  # Esperado: False