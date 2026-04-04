class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr, res = [],[]
        self.helper(0,nums,curr,res)
        return res

    def helper(self,i,nums,curr,res):
        if i == len(nums):
            res.append(curr)
            return
        self.helper(i+1,nums,curr.copy(),res)
        currcopy = curr.copy()
        currcopy.append(nums[i])
        self.helper(i+1,nums,currcopy,res)

        