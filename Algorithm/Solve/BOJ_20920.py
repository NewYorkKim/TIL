import sys
from collections import Counter 
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()
for _ in range(n):
    word = input().strip()
    
    if len(word) < m:
        continue

    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])

