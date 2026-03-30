class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m ={}
        for i in nums:
            if i not in m.keys():
                m[i]=1
            else:
                return True
        return False