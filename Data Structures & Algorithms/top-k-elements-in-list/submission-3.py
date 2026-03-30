class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqList = [[] for num in nums]
        res = []
        for num , freq  in count.items():
            freqList[freq-1].append(num)
        for num in range(len(nums)-1,-1,-1):
            if freqList[num]!=[]:
                res.extend(freqList[num])
            if len(res)>= k:
                break
        return res[:k+1]