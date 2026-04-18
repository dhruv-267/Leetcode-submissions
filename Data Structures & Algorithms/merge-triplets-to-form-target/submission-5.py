class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = {}                 # or valid = set()
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue 
            for i,n in enumerate(t):
                if target[i]==n:
                    valid[i]=n      #valid.add(i)
        return len(valid)==3
