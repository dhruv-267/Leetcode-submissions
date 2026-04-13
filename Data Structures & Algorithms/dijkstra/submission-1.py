class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = { i:[] for i in range(n)}
        for n1,n2,w in edges:
            adj[n1].append((w,n2))
        
        shortest = {}
        minheap = [(0,src)]
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for w2,n2 in adj[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(minheap,(w1+w2,n2))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
