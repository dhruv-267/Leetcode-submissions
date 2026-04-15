class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            choice1,choice2 = 0,0
            for i,n in enumerate(nums):
                nums[i] = max(n+choice1,choice2)
                choice1 = choice2
                choice2 = nums[i]
            return choice2
        
        return max(helper(nums[:len(nums)-1]),helper(nums[1:]),nums[0]) #why nums[0]
        # because if any nums array has only 1 element, 
        #then both [:len(num)-1] and [1:] will provide [] as input param to helper function 
        #since we are returning choice2 as answer in helper function,
        #[] will cause no iteration in loop and value of choice2 will remain 0.
        #thus both function calls will return 0, which is incorrect! 
        #so we manually add nums[0] to max() for such edge case.