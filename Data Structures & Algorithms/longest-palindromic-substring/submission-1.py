class Solution:
    def longestPalindrome(self, s: str) -> str:
        #brute force : O(n^3)

        #O(n^2) solution : at each index check if palindrome and widen left,right range
        n = len(s)
        res = [0,0] # 0,0 because inputstring s has atleast 1 character and each char is palindrome itself

        for i in range(n):
            #odd len palindrome
            l,r = i,i
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1) > (res[1]-res[0]+1) : res = [l,r]
                l-=1
                r+=1

            #even len palindrome
            l,r = i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1) > (res[1]-res[0]+1) : res = [l,r]
                l-=1
                r+=1
        
        return s[res[0]:res[1]+1] # res[1] + 1 because s[:] is non-exclusive for end value.