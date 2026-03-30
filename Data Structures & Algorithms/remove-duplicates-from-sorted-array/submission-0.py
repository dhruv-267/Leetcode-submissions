class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            if i!=nums[k]:
                k+=1
                nums[k]=i
        return k+1

        