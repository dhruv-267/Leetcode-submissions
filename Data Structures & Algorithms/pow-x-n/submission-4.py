class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            res = helper(x*x,n//2)
            return res*x if n%2 else res
        
        if n<0:
            x = 1/x
            n=-n
        return helper(x,n)