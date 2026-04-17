from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #time complexity for this solution is not n*target
        #because our total can exceed target any moment
        # max value total can get is sum(abs(n) for n in nums)
        # abs(n) because we are allowed to either add +n or -n to total,
        # so in best case scenario, for all n<0 we will add -n to our total
        #this way they will add up to increase our total more than just sum(nums) which might be -ve also.
        
        dp = {0:1} # sum : count
        # take 0 elements from nums,that totals to 0 => 1 way  sum([]) = 0

        for n in nums:
            curdp = {}
            for total,count in dp.items():
                curdp[total+n] = count + curdp.get(total+n,0)
                curdp[total-n] = count + curdp.get(total-n,0)
            dp = curdp
        return dp.get(target, 0)

        
        '''
        n = len(nums)
        total = 0
        @lru_cache(maxsize=None)
        def dfs(i,total):
            if i == n and total == target:
                return 1
            if i==n:
                return 0
            return dfs(i+1,total+nums[i]) + dfs(i+1,total-nums[i])
        
        res = dfs(0,0)
        dfs.cache_clear()
        return res
        '''