from typing import List
import typing

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtracking(k, i, j):
            if word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            res = False
            for d in directions:
                new_i = d[0] + i
                new_j = d[1] + j

                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    if (new_i, new_j) not in visited:
                        if backtracking(k + 1, new_i, new_j):
                            res = True
                            break
            visited.remove((i, j))
            return res

        if len(board) == 0 or len(board[0]) == 0:
            return False
        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if backtracking(0, i, j):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    res= solution.exist(board, word)
    print(res)