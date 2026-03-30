class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {'}':'{',')':'(',']':'['}
        for c in s:
            if c not in pmap:
                stack.append(c)
            else:
                if stack == []:
                    return False
                if stack.pop() != pmap[c]:
                    return False
            
        if stack != []:
            return False
        else: return True
