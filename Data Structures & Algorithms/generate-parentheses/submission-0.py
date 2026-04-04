class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ''
        openp, closep = 0,0

        def dfs(openp,closep,n,path):
            if openp == closep == n:
                res.append(path)
                return
            if openp<n:
                dfs(openp+1,closep,n,path+"(")
            if closep<openp:
                dfs(openp,closep+1,n,path+")")
        dfs(openp,closep,n,path)
        return res
        