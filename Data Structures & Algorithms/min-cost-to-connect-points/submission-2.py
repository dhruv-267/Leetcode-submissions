class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = { i:[] for i in range(n) }
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        visited = set()
        minHeap = [[0,0]]
        cost = 0
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            cost+=w1
            for w2,n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,[w2,n2])
        return cost
