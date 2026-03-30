class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        prefixsum = 0
        result = 0
        for i in nums:
            prefixsum+=i
            if prefixsum - k in prefix:
                result+=prefix[prefixsum-k]
            prefix[prefixsum] = prefix.get(prefixsum,0)+1
        return result