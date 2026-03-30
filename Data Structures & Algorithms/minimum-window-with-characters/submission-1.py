class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countS , countT = {}, {}
        reslen = math.inf
        res = [0,0]
        for char in t:
            countT[char] = 1 + countT.get(char,0)
        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have +=1
            while have == need :
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l, r+1]
                countS[s[l]]-=1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        if reslen != math.inf:
            return s[res[0]:res[1]]
        else:
            return ""
        