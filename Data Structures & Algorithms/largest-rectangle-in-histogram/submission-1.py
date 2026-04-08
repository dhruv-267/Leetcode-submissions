class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(height,index)
        maxarea = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][0]>heights[i]:
                popHeight , popIndex = stack.pop()
                area = (i-popIndex)*popHeight
                maxarea = max(area,maxarea)
                index =popIndex
            stack.append((heights[i],index))
        
        for height ,index in stack:
            maxarea = max((len(heights)-index)*height,maxarea)
        return maxarea



        