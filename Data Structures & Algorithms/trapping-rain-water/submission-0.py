class Solution:
    def trap(self, height: List[int]) -> int:
        maxheight = [0]*len(height)
        res = 0
        leftmax = 0
        for i in range(len(height)):
            maxheight[i] = leftmax
            leftmax = max(leftmax,height[i])
        rightmax = 0 
        for i in range(len(height)-1,-1,-1):
            maxheight[i] = min(maxheight[i],rightmax)
            rightmax = max(rightmax,height[i])
            if maxheight[i] - height[i] > 0:
                res += (maxheight[i] - height[i])
        return res