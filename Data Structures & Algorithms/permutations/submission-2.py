class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(i,nums):
            if i == len(nums):
                return [[]]
            perms = dfs(i+1,nums)
            res = []
            for perm in perms:
                for j in range(len(perm)+1):
                    cp = perm.copy()
                    cp.insert(j,nums[i])
                    res.append(cp)
            return res

        return dfs(0,nums)
        


        