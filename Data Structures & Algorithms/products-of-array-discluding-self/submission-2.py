class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodArr , revArr = [],[]
        prod, rev = 1,1
        for i in range(len(nums)):
            prod*=nums[i]
            prodArr.append(prod)
            rev*=nums[len(nums)-1-i]
            revArr.insert(0,rev)
        res = [revArr[1]]
        for i in range(1,len(nums)-1):
            res.insert(i , prodArr[i-1]*revArr[i+1])
        res.append(prodArr[-2])
        return res
