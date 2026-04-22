class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        n = len(num1)
        m = len(num2)
        carry = 0
        res = [0 for i in range(n+m)]

        for i in range(n):
            n1 = int(num1[i])
            for j in range(m):
                n2 = int(num2[j])
                multiply = n1*n2
                carry, digit = divmod(multiply+res[i+j],10)
                res[i+j] = digit
                res[i+j+1] += carry
        res.reverse()
        i = 0
        while res[i] == 0:
            i+=1
        res = res[i:]
        for i in range(len(res)):
            res[i] = str(res[i])
        
        return str("".join(res))
            


