class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]  #reverse nums arr for multiplication
        n, m = len(num1), len(num2)          

        res = [0 for i in range(n+m)]        # max number of digits in result can be len(num1)+len(num2)


        for i in range(n):
            n1 = int(num1[i]) #int()
            for j in range(m):
                n2 = int(num2[j]) #int()
           
                multiply = n1*n2
                carry, digit = divmod(multiply+res[i+j],10)
                res[i+j] = digit
                res[i+j+1] += carry

        res.reverse() # reverse res to return final ans

        i = 0         # remove preceding Zeros
        while res[i] == 0:
            i+=1
        res = res[i:]

        for i in range(len(res)):  #convert each int digit to str as join() only works on strings datatype
            res[i] = str(res[i])
        
        return "".join(res)
            


