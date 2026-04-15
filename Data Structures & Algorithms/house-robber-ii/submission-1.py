class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            choice1,choice2 = 0,0
            for i,n in enumerate(nums):
                nums[i] = max(n+choice1,choice2)
                choice1 = choice2
                choice2 = nums[i]
            return choice2
        
        return max(helper(nums[:len(nums)-1]),helper(nums[1:]),nums[0])