# class Solution(object):
#     def maximumWealth(self, accounts):
#         ans = 0

#         for i in range(len(accounts)):
#             tmp = sum(accounts[i])

#             if tmp > ans:
#                 ans = tmp

#         return ans

class Solution(object):
    def maximumWealth(self, accounts):
        ans = 0

        for i in range(len(accounts)):
            ans = max(ans, sum(accounts[i]))

        return ans