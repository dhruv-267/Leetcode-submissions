class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        res = 0
        l = 0
        mostfreq = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            mostfreq = hashmap[Counter(hashmap).most_common(1)[0][0]]
            if (r-l+1) - mostfreq > k :
                hashmap[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
        return res



        