class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res =[]
        remainder, carry = 0,1
        digits.reverse()
        for i in range(len(digits)):
            carry , remainder = divmod(digits[i]+carry,10)
            res.append(remainder)
        if carry:
            res.append(carry)
        res.reverse()
        return res