from typing import List
# time complexity: O(S) S is the length of all solutions
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(res, comb, begin, target):
            if target == 0:
                res.append(comb[:])
                return

            for i in range(begin, n):
                rest = target - candidates[i]
                if rest < 0:
                    break
                backtracking(res, comb+[candidates[i]], i, rest)

        n = len(candidates)
        if n == 0:
            return []
        res = []
        candidates.sort()
        backtracking(res, [], 0, target)
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum([2,3,6,7], 7)
    print(res)