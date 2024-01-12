from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        que = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == "O":
                        board[i][j] = "Y"
                        que.append((i, j))

        while que:
            x, y = que.popleft()

            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O":
                    board[nx][ny] = "Y"
                    que.append((nx, ny))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"