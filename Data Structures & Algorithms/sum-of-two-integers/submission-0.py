class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carrybit = 0
        for i in range(32):
            bit1 = (a>>i) & 1
            bit2 = (b>>i) & 1
            sumbit = bit1^bit2^carrybit
            carrybit = (bit1 & bit2) | (bit1 & carrybit) | (bit2 & carrybit) #if any 2 bits from 3 bits above are 1 then the sum will be >=2 (0010) so we will have carrybit = 1 for next index.
            if sumbit:     #only have to do this if sumbit is 1
                res = res | (sumbit<<i)

        res = res& 0xFFFFFFFF
        if res > (1<<31):
            res = ~ (res^0xFFFFFFFF)

        return res
            

        