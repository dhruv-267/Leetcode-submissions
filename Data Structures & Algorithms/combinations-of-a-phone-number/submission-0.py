class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        charmap = {
            "2" : "ABC",
            "3" : "DEF",
            "4" : "GHI",
            "5" : "JKL",
            "6" : "MNO",
            "7" : "PQRS",
            "8" : "TUV",
            "9" : "WXYZ"
        }
        
        def dfs(i,cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            
            for c in charmap[digits[i]]:
                dfs(i+1,cur+c.lower())
            
        if digits:
            dfs(0,"")
        return res