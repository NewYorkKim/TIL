import re, collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub("[^\w]", " ", paragraph).lower().split() if word not in banned]

        words_count = collections.Counter(words)
        
        return words_count.most_common(1)[0][0]