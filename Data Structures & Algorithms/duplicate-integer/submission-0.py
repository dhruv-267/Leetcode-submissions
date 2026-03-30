class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if i in map.keys():
                return True
            map[i]= 0
        return False