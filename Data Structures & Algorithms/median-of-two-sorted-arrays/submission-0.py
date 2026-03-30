class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total // 2

        if len(nums1) <= len(nums2):
            a,b = nums1, nums2
        else:
            a,b = nums2, nums1
        
        low, high = 0, len(a) - 1

        while True:
            mid = (low+high)//2
            bhalf = half - mid -2

            aleft = a[mid] if mid >=0 else -math.inf
            aright = a[mid+1] if mid+1 < len(a) else math.inf
            bleft = b[bhalf] if bhalf >= 0 else -math.inf
            bright = b[bhalf+1] if bhalf+1 < len(b) else math.inf

            if aleft<=bright and bleft<=aright:
                if total%2 == 1:
                    return float(min(aright,bright))
                else:
                    return (max(aleft,bleft)+min(aright,bright))/2.0
            elif aleft>bright:
                high = mid -1
            else:
                low = mid + 1