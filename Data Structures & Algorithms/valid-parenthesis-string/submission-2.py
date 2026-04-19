class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left, max_left = 0,0

        for c in s:
            if c == "(":
                min_left += 1
                max_left += 1
            elif c ==")":
                min_left -= 1
                max_left -= 1
            else:
                min_left -= 1
                max_left += 1
            if max_left <0:
                return False
            if min_left <0:
                min_left = 0
        return min_left ==0