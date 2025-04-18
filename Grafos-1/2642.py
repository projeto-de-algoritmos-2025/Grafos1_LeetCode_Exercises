import heapq

class Graph:
    def __init__(self, n, edges):
        """
        :param n: Número de nós.
        :param edges: Lista de arestas representadas por [from, to, edgeCost].
        """
        self.graph = {i: [] for i in range(n)}  
        for u, v, cost in edges:
            self.graph[u].append((v, cost))

    def addEdge(self, edge):
        """
        Adiciona uma aresta ao grafo.
        :param edge: Uma lista de 3 inteiros [from, to, edgeCost].
        """
        u, v, cost = edge
        self.graph[u].append((v, cost))

    def shortestPath(self, node1, node2):
        """
        Encontra o caminho mais curto entre node1 e node2.
        :param node1: Nó inicial.
        :param node2: Nó final.
        :return: O custo mínimo do caminho ou -1 se não houver caminho.
        """
      
        pq = [(0, node1)]  
        dist = {i: float('inf') for i in self.graph}  
        dist[node1] = 0
        
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            
            if current_node == node2:
                return current_dist  

           
            for neighbor, weight in self.graph[current_node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:  
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return -1  




graph = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])


print(graph.shortestPath(3, 2))  
print(graph.shortestPath(0, 3))  


graph.addEdge([1, 3, 4])


print(graph.shortestPath(0, 3))  
