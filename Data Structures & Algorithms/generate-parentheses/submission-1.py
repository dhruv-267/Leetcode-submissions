class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opening,closing,n,path):
            #base case : number of both opening and closing para = n
            if opening == closing == n:
                res.append(path)
                return
            # number of opening para is less than n -> add "(" to path, opening+=1
            if opening<n:
                dfs(opening+1,closing,n,path+"(")
            #if number of closing para is less than #of opening para then only add ")" to path, closing+=1
            if closing<opening:
                dfs(opening,closing+1,n,path+")")
        dfs(0,0,n,"")
        return res
        