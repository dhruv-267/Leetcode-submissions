class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_seen = 0
        for i in range(len(nums)):
            if max_seen<i:
                return False
            max_seen  = max(max_seen,i + nums[i])

    
        return True