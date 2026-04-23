class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in numset: #(O(1)) 
                seqlen = 1
                while num+seqlen in numset: #(O(1))
                    seqlen+=1
                longest = max(longest,seqlen)
        return longest