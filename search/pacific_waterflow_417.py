from typing import List
# find path from (i,j) to pacific is hard, so we find path from pacific and atlantic to (i,j)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def search(starts):
            def dfs(i, j):
                if (i,j) in visited:
                    return
                visited.add((i,j))
                for nx, ny in ((i,j+1),(i,j-1),(i-1,j),(i+1,j)):
                    if 0<=nx<m and 0<=ny<n and heights[nx][ny]>=heights[i][j]:
                        dfs(nx,ny)
            visited = set()
            for i, j in starts:
                dfs(i, j)
            return visited

        if len(heights) == 0 or len(heights[0]) == 0:
            return
        m, n= len(heights), len(heights[0])
        pacific = [(i,0)for i in range(m)] + [(0,i) for i in range(n)]
        atlantic = [(i,n-1) for i in range(m)] + [(m-1,i) for i in range(n)]
        res = list(map(list, search(pacific) & search(atlantic)))
        return res

if __name__ == '__main__':
    solution = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    res = solution.pacificAtlantic(heights)
    print(res)