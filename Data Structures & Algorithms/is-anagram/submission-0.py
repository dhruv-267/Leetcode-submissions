class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map = {}
        for i in range(len(s)):       
            map[s[i]] = map.get(s[i], 0) + 1
            map[t[i]] = map.get(t[i], 0) - 1
        for v in map.values():
            if v != 0:
                return False
        return True       