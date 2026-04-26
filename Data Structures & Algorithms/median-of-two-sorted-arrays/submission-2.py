class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        total = len(a)+len(b)
        half = total//2

        if len(a)>len(b):
            a,b = b,a
        
        low,high = 0, len(a)-1
        while True:
            amid = (low+high)//2
            bmid = half - amid -2

            aleft = a[amid] if amid>=0 else -math.inf
            bleft = b[bmid] if bmid >= 0 else -math.inf
            aright = a[amid+1] if amid+1 < len(a) else math.inf
            bright = b[bmid+1] if bmid+1 <len(b) else math.inf

            if aleft<=bright and bleft<=aright:
                if total%2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft)+ min(aright,bright))/2
            
            elif aleft>bright:
                high = amid - 1
            else:
                 low = amid + 1
