from collections import deque

n = int(input())
seqs = list(map(int, input().split()))
balloons = deque([(seq, idx + 1) for idx, seq in enumerate(seqs)])
result = []

while True:
    target = balloons.popleft()
    result.append(target[1])
    point = target[0]

    if len(balloons) == 0:
        break

    if point > 0:
        for i in range(point-1):
            tmp = balloons.popleft()
            balloons.append(tmp)
    else:
        for i in range(point, 0, 1):
            tmp = balloons.pop()
            balloons.appendleft(tmp)
        
print(*result)