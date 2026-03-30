class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num,0)+1
        sort_hm = dict(sorted(hm.items(), key = lambda item : item[1],reverse=True))
        return list(sort_hm.keys())[:k]