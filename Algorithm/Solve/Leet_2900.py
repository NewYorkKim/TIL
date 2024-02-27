class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = []

        for i in range(n):
            tmp = []
            prev = -1
            for j in range(i, n):
                if j == i:
                    tmp.append(words[j])
                    prev = groups[j]
                else:
                    if prev != groups[j]:
                        tmp.append(words[j])
                        prev = groups[j]
            if len(tmp) > len(dp):
                dp = tmp

        return dp