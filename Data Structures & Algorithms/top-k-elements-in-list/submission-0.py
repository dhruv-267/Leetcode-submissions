class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = map.get(n,0)+1
        map = dict(sorted(map.items(),key =lambda item:item[1], reverse = True))
        return list(map.keys())[:k]