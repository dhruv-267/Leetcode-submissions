class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        maps , mapt = {},{}
        reslen,res = float("inf"), [0,0]
        for c in t:
            mapt[c] = 1 + mapt.get(c,0)
        have , need = 0 , len(mapt)
        l = 0
        for r in range(len(s)):
            maps[s[r]] = 1 + maps.get(s[r],0)
            if s[r] in mapt and maps[s[r]] == mapt[s[r]]:
                have+=1
            while have == need:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = [l, r + 1]
                maps[s[l]]-=1
                if s[l] in mapt and maps[s[l]]==mapt[s[l]]-1:
                    have-=1
                l+=1
        return s[res[0]:res[1]] if reslen != float("inf") else ""