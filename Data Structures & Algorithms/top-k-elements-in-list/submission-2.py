class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqArr = [[] for num in nums]
        print(freqArr)
        for i, j in count.items():
            print(i,j)
            freqArr[j-1].append(i)
        print(freqArr)
        res = []
      
        for i in range(len(freqArr)-1,-1,-1):
            if freqArr[i]!= []:
                res.extend(freqArr[i])
            if len(res)>=k:
                break
        return res[0:k]

        