class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        res,total = 0,0
        for num in nums:
            total +=num
            diff = total - k
            res += prefixSums.get(diff,0)
            prefixSums[total] = prefixSums.get(total,0)+1
        return res
    
