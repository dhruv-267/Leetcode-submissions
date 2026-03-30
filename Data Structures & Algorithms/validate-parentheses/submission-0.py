class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}":"{",']':'[',')':'('}
        stack = []
        for c in s:
            if c not in ['}',']',')']:
                stack.append(c)
            else:
                if not len(stack):
                    return False
                x = stack.pop()
                if x!=map[c]:
                    return False
        if len(stack):
            return False
        return True