from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def visit(airport):
            while graph[airport]:
                next_stop = heapq.heappop(graph[airport])
                visit(next_stop)
            route.append(airport)

        visit("JFK")

        return route[::-1]
sol = Solution()

print(sol.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))

print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],
                         ["ATL","JFK"],["ATL","SFO"]]))