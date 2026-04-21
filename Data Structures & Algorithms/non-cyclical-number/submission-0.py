class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            output = 0
            while n:
                div , mod = divmod(n,10)
                n = div
                output += mod*mod
            return output

        visited = set()

        while n not in visited:
            visited.add(n)
            n = sos(n)
        return True if n ==1 else False
        
        
