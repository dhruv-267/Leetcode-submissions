class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqList = [[] for num in nums]
        
        for num , freq  in count.items():
            freqList[freq-1].append(num)
        count = []
        for num in range(len(nums)-1,-1,-1):
            count.extend(freqList[num])
            if len(count)>= k:
                break
        return count[:k+1]