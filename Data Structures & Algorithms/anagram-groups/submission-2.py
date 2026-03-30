class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            chararr = [0]*26
            for c in s:
                chararr[ord(c)-ord("a")]+=1
            if tuple(chararr) not in map:
                map[tuple(chararr)] = [s]
            else:
                map[tuple(chararr)].append(s)
        
        return list(map.values())


