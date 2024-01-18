class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])

        for i in range(numRows-1):
            tmp = [1]
            for j in range(i):
                tmp.append(ans[i][j] + ans[i][j+1])
            tmp.append(1)
            ans.append(tmp)
        
        return ans