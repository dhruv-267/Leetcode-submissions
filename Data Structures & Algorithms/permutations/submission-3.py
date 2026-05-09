class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        for num in nums:
            res = []
            for perm in perms:
                for i in range(len(perm)+1):
                    copy = perm.copy()
                    copy.insert(i,num)
                    res.append(copy)
            perms = res
    
        return perms
    
    '''
        def dfs(i,nums):
            if i == len(nums):
                return [[]]
            perms = dfs(i+1,nums)
            res = []
            for perm in perms:  #n!
                for j in range(len(perm)+1):  #n
                    cp = perm.copy()
                    cp.insert(j,nums[i]) # O(n)
                    res.append(cp)
            return res

        return dfs(0,nums)
    '''





        