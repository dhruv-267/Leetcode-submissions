class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total/2

        sumset = set()
        sumset.add(0)
        for n in nums: 
            for num in sumset.copy(): # 
                if num+n==target:
                    return True
                sumset.add(num+n)
        return False
