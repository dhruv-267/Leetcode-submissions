class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])
        res = []
        for perm in perms:
            for i in range(len(perm)+1):
                co_py = perm.copy()
                co_py.insert(i,nums[0])
                res.append(co_py)
        return res

        