class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[index,temp] 

        for i , temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                index , tmp = stack.pop()
                res[index] = i - index
            stack.append([i,temp])
        return res


        