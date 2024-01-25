import sys
input = sys.stdin.readline

n = int(input())
nodes = [tuple(map(int, input().split())) for _ in range(n-1)]
graphs = {i+1: [] for i in range(n)}

for node in nodes:
    graphs[node[0]].append(node[1])
    graphs[node[1]].append(node[0])

res = [0] * n

for i in range(1, n+1):
    tmp = []
    if res[i-1] == 0:
        tmp.append(i)
        while tmp:
            parent = tmp.pop(0)

            for node in graphs[parent]:
                if res[node-1] == 0:
                    tmp.append(node)
                    res[node-1] = parent

for i in res[1:]:
    print(i)