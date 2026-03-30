class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum = 0
        hashmap = {}

        for num in nums:
            hashmap[num] = 1

        for num in nums:
            if num-1 not in hashmap:
                length = 1
                while num+length in hashmap:
                    length+=1
                maximum = max(maximum,length)
        
        return maximum

