import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cases = []
    
    for i in range(n):
        for j in range(i, m):
            cases.append((i+1, j+1))
    
    print(len(cases))
            