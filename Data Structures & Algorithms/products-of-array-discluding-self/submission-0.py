class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = []
        preProd.append(nums[0])
        postProd = []
        postProd.append(nums[-1])

        for i in range(1,len(nums)):
                preProd.append(preProd[-1]*nums[i])

        for i in range(len(nums)-2,-1,-1):
            postProd.insert(0,postProd[0]*nums[i])

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postProd[1])
            elif i == len(nums)-1:
                result.append(preProd[len(nums)-2])
            else:
                result.append(preProd[i-1]*postProd[i+1])
        
        return result