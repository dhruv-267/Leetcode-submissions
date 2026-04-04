class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        reslist = []
        self.helper(0,nums,[],reslist)
        return reslist

    def helper(self,i,nums,currlist,reslist):
        if i == len(nums):
            reslist.append(currlist)
            return
        
        currcopy = currlist.copy()
        currcopy.append(nums[i])
        self.helper(i+1,nums,currcopy,reslist)
        currcopy = currlist.copy()
        self.helper(i+1,nums,currcopy,reslist)
            

