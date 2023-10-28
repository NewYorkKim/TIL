import sys
input = sys.stdin.readline

n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graphs[i][k] == 1 and graphs[k][j] == 1:
                graphs[i][j] = 1

for graph in graphs:
    print(*graph)