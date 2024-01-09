class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.checkVertical(board) == False:
            return False
        elif self.checkHorizontal(board) == False:
            return False
        elif self.checkSquare(board) == False:
            return False
        
        return True
        
    def checkVertical(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i].count(board[i][j]) != 1:
                        return False
        return True
        
    def checkHorizontal(self, board: List[List[str]]) -> bool:
        tmp = [[] for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                tmp[j].append(board[i][j])
            
        return self.checkVertical(tmp)
        
    def checkSquare(self, board: List[List[str]]) -> bool:
        tmp = [[] for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board)):
                tmp[(i//3)*3+(j//3)].append(board[i][j])
                
        return self.checkVertical(tmp)