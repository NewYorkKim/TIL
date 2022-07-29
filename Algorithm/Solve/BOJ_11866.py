from collections import deque

n, k = map(int, input().split())
que = deque(range(1, n+1))
result = []

for i in range(len(que)):
    for j in range(k):
        if j == k-1:
            m = que.popleft()
            result.append(m)
        else:
            m = que.popleft()
            que.append(m)

print('<' + str(result)[1:-1] + '>')