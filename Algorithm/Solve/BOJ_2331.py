import sys
from collections import deque
input = sys.stdin.readline

a, p = map(int, input().split())
idx, results = 0, [a]

while True:
    res = 0
    tmp = results[idx]

    for i in range(len(str(tmp))):
        res += (tmp % 10) ** p
        tmp //= 10

    if res in results:
        print(results.index(res))
        break
    else:
        results.append(res)
        idx += 1