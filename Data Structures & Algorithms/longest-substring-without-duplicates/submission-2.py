class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i , j = 0 , 0
        hashmap = {}
        res = 0
        while j < len(s):
            if s[j] not in hashmap:
                hashmap[s[j]] = 1
                res = max(res,j-i+1)
                j += 1
            else:
                while s[j] in hashmap:
                    del hashmap[s[i]]
                    i+=1
                hashmap[s[j]] = 1
                res = max(res,j-i+1)
                j+=1
        return res