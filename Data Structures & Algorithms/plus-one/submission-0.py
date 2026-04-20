class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res =[]
        remainder, carry = 0,0
        digits.reverse()
        for i in range(len(digits)):
            if i==0:
                digits[i]+=1
            carry , remainder = divmod(digits[i]+carry,10)
            res.insert(0,remainder)
        if carry:
            res.insert(0,carry)
        return res
                