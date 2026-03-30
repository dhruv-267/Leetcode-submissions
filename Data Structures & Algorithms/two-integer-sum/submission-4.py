class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = {}
        for i in range(len(nums)):
            if target - nums[i] in numsdict:
                return [numsdict[target-nums[i]],i]
            numsdict[nums[i]] = i