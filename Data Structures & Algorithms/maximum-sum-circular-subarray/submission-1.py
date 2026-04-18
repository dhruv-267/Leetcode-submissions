class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # max sum of circular array = total sum - min sum subarray in middle
        # OR just flatten/normal array max sum.. which ever is bigger

        maxsum,minsum = nums[0],nums[0]
        curmax , curmin = 0,0
        total = 0
        for n in nums:
            curmax = max(0,curmax)+n
            maxsum = max(maxsum,curmax)
            curmin = min(0,curmin)+n
            minsum = min(minsum,curmin)
            total += n

        # most vital check..if all values in array are -ve.
        # minsum will be equal to total.. so total-minsum will be 0
        # in such case [] = 0 will be returned instead of returning non empty maxsum array.
        # which is logically incorrect
        if maxsum < 0:  #if maxsum itself is <0 it means all values in array are less then 0
            return maxsum 

        return max(maxsum,total-minsum) 