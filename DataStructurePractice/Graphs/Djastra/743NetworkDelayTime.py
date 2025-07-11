import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Dijkstra
        heap = [(0, k)]  # (distance, node)
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time

            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + wt, nei))

        # Step 3: Final check
        if len(dist) == n:
            return max(dist.values())
        else:
            return -1