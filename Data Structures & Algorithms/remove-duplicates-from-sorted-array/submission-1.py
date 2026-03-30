class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if nums[i]!=n:
                i+=1
                nums[i]=n
        return i+1
        