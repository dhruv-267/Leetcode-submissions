class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        low , high = 0, len(nums) -1
        res = math.inf
        while low <=high:
            mid = (low + high)//2
            res = min(res,nums[mid])
            #mid in left rotated:
            if nums[mid] >= nums[0]:
                res = min(res,nums[0])
                low = mid + 1
            #or
            #mid in right rotated:
            else: 
                high = mid -1
        return res