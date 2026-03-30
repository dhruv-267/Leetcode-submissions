class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {'}':'{',')':'(',']':'['}
        for c in s:
            if c in pmap:
                if stack == []:
                    return False
                elif stack.pop() != pmap[c]:
                    return False
            else:
                stack.append(c)
        if stack != []:
            return False
        else: return True
