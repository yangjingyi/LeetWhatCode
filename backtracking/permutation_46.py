# permutation
import typing
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, ans, level):
            if level == len(nums) - 1:
                ans.append(nums[:])
            for i in range(level, len(nums)):
                nums[i], nums[level] = nums[level], nums[i]
                backtracking(nums, ans, level+1)
                nums[i], nums[level] = nums[level], nums[i]
        ans = []
        backtracking(nums, ans, 0)
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    res = solution.permute(nums)
    print(res)