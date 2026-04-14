class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append([w,v])
        
        visited = set()
        minHeap = [[0,k]]
        total = 0

        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            if v1 in visited:
                continue
            visited.add(v1)
            total = max(total,w1)

            for w2,v2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(minHeap,[w1+w2,v2])
        
        return total if len(visited) == n else -1

        