class Solution:
    def rob(self, nums: List[int]) -> int:
        choice1, choice2 = 0 , 0
        for i,n in enumerate(nums):
            nums[i] = max(n + choice1, choice2)
            choice1 = choice2
            choice2 = nums[i]
        return nums[-1]