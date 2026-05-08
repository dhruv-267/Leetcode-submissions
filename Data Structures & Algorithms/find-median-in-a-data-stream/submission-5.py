class MedianFinder:

    def __init__(self):
        self.small = []  #max heap of smaller values  (-ve values)
        self.large = []  #min heap of larger values     
        heapq.heapify(self.small)
        heapq.heapify(self.large)   

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1 * num)

        if self.small and self.large and (-1 * self.small[0] > self.large[0]) :
            heapq.heappush(self.large,-1 * heapq.heappop(self.small))   

        if len(self.small) > len(self.large)+1 :
            heapq.heappush(self.large,-1 * heapq.heappop(self.small))
        if len(self.large) > len(self.small)+1 :
            heapq.heappush(self.small,-1 * heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large)> len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0] )/2
        
        