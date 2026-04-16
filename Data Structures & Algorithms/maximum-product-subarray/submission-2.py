class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #as it contains -ve values res can not be initialises to 0
        res = nums[0]
        curmax , curmin = 1 , 1

        for n in nums:
            temp = curmax * n
            curmax = max(n,temp,curmin*n)
            curmin = min(n,temp,curmin*n)
            res = max(res,curmax)
        return res