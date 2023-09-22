import sys
import string
input = sys.stdin.readline

s = input()
q = int(input())

counts = {}
for chr in string.ascii_lowercase:
    counts[chr] = [0]
    count = 0
    
    for i in range(len(s)):
        if s[i] == chr:
            count += 1
        counts[chr].append(count)

for _ in range(q):
    conditions = input().split()
    a, l, r = conditions[0], int(conditions[1]), int(conditions[2])
    
    print(counts[a][r+1] - counts[a][l])