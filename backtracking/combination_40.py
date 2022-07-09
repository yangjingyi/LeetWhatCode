from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(begin, comb, res, rest):
            if rest == 0:
                res.append(comb[:])
                return
            for i in range(begin, n):
                if candidates[i] > rest:
                    break
                # without this limit, there will be the same combinations in the final result
                if i > begin and candidates[i - 1] == candidates[i]:
                    continue
                comb.append(candidates[i])
                backtracking(i + 1, comb, res, rest - candidates[i])
                comb.pop()

        if len(candidates) == 0:
            return []
        n = len(candidates)

        res = []
        comb = []
        candidates.sort()
        backtracking(0, comb, res, target)
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = solution.combinationSum2(nums, target)
    print(res)