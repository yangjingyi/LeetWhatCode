from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(n, k, idx, res, comb):
            if len(comb) == k:
                res.append(comb[:])
            for i in range(idx, n+1):
                if i > n-(k-len(comb))+1:
                    break
                comb.append(i)
                backtracking(n,k,i+1, res, comb)
                comb.pop()
        res = []
        comb = []
        if n <0 or n<k:
            return []
        backtracking(n, k, 1, res, comb)
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.combine(4,2)
    print(res)