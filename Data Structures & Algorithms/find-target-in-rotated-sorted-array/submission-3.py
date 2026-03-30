class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low , high = 0 , len(nums)-1

        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            #mid in left rotated arr
            if nums[mid]>=nums[0]:
                if target > nums[mid] or target < nums[0]:
                    low = mid + 1
                else:
                    high = mid - 1

            #mid in right rotated arr
            else:
                if target < nums[mid] or target > nums[-1]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1