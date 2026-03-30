class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for n in nums:
            cursum = max(cursum,0) + n
            maxsum = max(maxsum,cursum)
        return maxsum
    
      