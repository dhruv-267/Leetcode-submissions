class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
                return 1

        if n<0:
            x = 1/x
            n = -n

        def helper(x,n):
            
            if n == 0:
                return 1
            
            res = helper(x*x,n//2)
            return res*x if n%2 else res

        return helper(x,n)
        