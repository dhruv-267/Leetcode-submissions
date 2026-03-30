class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            if (num-1) not in numset:
                i = 1
                while (num+i) in numset:
                    i+=1
                res = max(res,i)
        return res
        