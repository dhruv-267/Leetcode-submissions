class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)
        res = max(piles)
        while low <=high:
            mid = (low+high)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time > h:
                low = mid+1
            elif time <= h:
                high = mid-1
                res = min(res,mid)
        return res

        