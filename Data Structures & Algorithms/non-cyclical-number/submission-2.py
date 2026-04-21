class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            output = 0
            while n:
                div , mod = divmod(n,10)
                n = div
                output += mod*mod
            return output
        '''
        # T : O(logn) S: 0(logn)
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sos(n)
        return True if n ==1 else False
        '''
        # T:O(logn) S: O(1)
        slow,fast = n,sos(n)
        while slow!=fast:
            fast = sos(fast)
            fast = sos(fast)
            slow = sos(slow)
        return True if fast == 1 else False
        
