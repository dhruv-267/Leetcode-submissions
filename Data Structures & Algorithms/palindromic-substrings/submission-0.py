class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            #odd len palindrome
            l,r = i,i
            while l>=0 and r<n and s[l]==s[r]:
                res+=1
                l-=1
                r+=1

            #even len palindrome
            l,r = i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        
        return res