# permutation
import typing
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, ans, level, vis, perm):
            if len(perm) == len(nums):
                ans.append(perm[:])
            for i in range(len(nums)):
                if vis[i] or (i>0 and not vis[i-1] and nums[i]==nums[i-1]):
                    continue
                vis[i] = True
                perm.append(nums[i])
                backtracking(nums, ans, level+1, vis, perm)
                perm.pop()
                vis[i] = False
        ans = []
        perm = []
        vis = [False] * len(nums)
        nums.sort()
        backtracking(nums, ans, 0, vis, perm)
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,3]
    res = solution.permuteUnique(nums)
    print(res)