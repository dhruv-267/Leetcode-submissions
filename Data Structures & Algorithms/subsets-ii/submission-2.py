class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cur, res = [], set()
        def dfs(i):
            if i == len(nums):
                res.add(tuple(cur.copy()))
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return list(res)
        