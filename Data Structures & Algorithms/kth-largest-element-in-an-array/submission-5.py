class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        heapq.heapify(nums)
        while len(nums)>k: 
            heapq.heappop(nums)
        return nums[0]
        """
        minn, maxn = min(nums), max(nums)
        freq = [0] * (maxn - minn + 1)
        for num in nums:
            freq[num-minn]+=1

        for i in range(len(freq)-1,-1,-1):
            k -= freq[i]
            if k<=0:
                return i + minn
