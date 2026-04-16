class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total/2

        sumset = set()
        sumset.add(0) # 0 indicates we have choice of not selecting any element randomly for sum subset.. so we can put 0 at its place
        for num in nums: #for each num in input array, we want to add it to every single element in sumset and append the sum to sumset 
            for n in sumset.copy(): #sumset.copy() because during iteration we are manipulating sumset by appending new values to sumset which will throw runtime error
                if num + n == target:
                    return True
                sumset.add( num + n )
        return False
