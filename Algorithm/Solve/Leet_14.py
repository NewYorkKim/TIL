class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        target = strs[0]
        ans = ""
        
        for i in range(len(target)):
            tmp = target[i]
            for j in range(1, len(strs)):
                if strs[j][i] != tmp:
                    return ans
            ans += tmp
        
        return ans