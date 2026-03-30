class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap.keys():
                hashmap[s[i]]=1
            else:
                hashmap[s[i]]+=1
            if t[i] not in hashmap.keys():
                hashmap[t[i]] = -1
            else:
                hashmap[t[i]]-=1

        for key in hashmap.keys():
            if hashmap[key]!=0:
                return False
        return True       