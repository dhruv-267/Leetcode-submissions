class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def dfs(i,nums):
            nonlocal res
            if i == len(nums):
                res = [[]]
                return
            dfs(i+1,nums)
            temp = []
            for j in range(len(res)):
                for x in range(len(res[j])+1):
                    updatedcopy = res[j].copy()
                    updatedcopy.insert(x,nums[i])
                    temp.append(updatedcopy)
            res = temp
        dfs(0,nums)
        return res
