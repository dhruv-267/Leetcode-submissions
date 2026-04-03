class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = list(Counter(tasks).values())
        count = [-c for c in count]
        heapq.heapify(count)
        q = collections.deque()
        time = 0
        while count or q:
            time+=1
            if count:
                val = heapq.heappop(count)
                if val +1 < 0:
                    q.append([val+1,time+n])
            if q and q[0][1]==time:
                heapq.heappush(count,q.popleft()[0])
        return time

        