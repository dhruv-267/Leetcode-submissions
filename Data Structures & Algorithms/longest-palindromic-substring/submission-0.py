class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = [0,0]
        for i in range(n):
            #odd len substrings
            l,r = i,i
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>(res[1]-res[0]+1): 
                    res = [l,r]
                l-=1
                r+=1

            #even len substrings
            l,r = i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>(res[1]-res[0]+1): 
                    res=[l,r]
                l-=1
                r+=1
        return s[res[0]:res[1]+1]