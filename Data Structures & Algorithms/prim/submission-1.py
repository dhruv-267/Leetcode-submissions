class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int: 
        adj = { i:[] for i in range(n)}
        for n1,n2,w in edges:
            adj[n1].append((n2,w))
            adj[n2].append((n1,w))
        
        visited = set()
        res = 0
        mst = []
        minheap = []
        for neighbor, w in adj[0]:
            minheap.append([w,0,neighbor])
        heapq.heapify(minheap)
        visited.add(0)

        while minheap and len(mst)<n-1:
            w,n1,n2 = heapq.heappop(minheap)
            if n2 in visited:
                continue
            visited.add(n2)
            mst.append([w,n1,n2])
            res+=w
            for neighbor,w_next in adj[n2]:
                if neighbor not in visited:
                    heapq.heappush(minheap,[w_next,n2,neighbor])
        
        return res if len(visited)==n else -1