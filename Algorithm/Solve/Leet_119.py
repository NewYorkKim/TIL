class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = []
        dp.append([1])

        for i in range(rowIndex):
            tmp = [1]
            for j in range(i):
                tmp.append(dp[i][j] + dp[i][j+1])
            tmp.append(1)
            dp.append(tmp)

        return dp[rowIndex]