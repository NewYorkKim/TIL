from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr).values()

        if len(cnt) == len(set(cnt)):
            return True
        else:
            return False