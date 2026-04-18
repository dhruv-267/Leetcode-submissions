from functools import lru_cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l ,r = 0,0
        res , farthest = 0,0
        while r < n-1:
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
                if farthest >= n-1:
                    return res+1
            l = r+1
            r = farthest
            res+=1
        return res

            

