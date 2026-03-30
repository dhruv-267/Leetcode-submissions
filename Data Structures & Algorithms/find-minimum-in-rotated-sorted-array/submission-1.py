class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]

        low , high = 0 , len(nums)-1
        res = nums[0]
        while low<=high:
            mid = (low+high)//2

            #mid in left sorted half
            if nums[mid] >= nums[0]:
                res = min(res, nums[0])
                low = mid+1
            #mid in right sorted half
            else:
                res = min(res, nums[mid])
                high = mid-1
        return res