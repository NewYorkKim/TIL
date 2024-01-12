from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    cnt += 1
        
        return cnt

    def dfs(self, grid, i, j):
        grid[i][j] = 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
 
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                self.dfs(grid, nx, ny)