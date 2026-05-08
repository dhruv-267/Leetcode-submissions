class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap = [] #minheap
        for i in range(len(capital)):
            cap.append([capital[i],profits[i]])
        heapq.heapify(cap)
        projects = [] #maxheap
        
        while k:
            while cap and cap[0][0] <= w :
                heapq.heappush(projects,-heapq.heappop(cap)[1])
            if not projects:
                break
            w += -heapq.heappop(projects)
            k-=1
        
        return w