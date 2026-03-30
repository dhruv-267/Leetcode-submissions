class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        for i, h in enumerate(heights):
            startindex = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea,height*(i-index))
                startindex = index 
            stack.append([startindex,h])

        for i,h in enumerate(stack):
            maxarea = max(maxarea, h[1]*(len(heights)-h[0]))
        return maxarea       