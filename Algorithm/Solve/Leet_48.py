class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        tmp = [[0] * len(matrix) for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                tmp[j][len(matrix) - (i + 1)] = matrix[i][j]
                
        matrix[:] = tmp
        