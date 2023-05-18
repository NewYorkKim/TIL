piece = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]
ans = []

for i in range(len(piece)):
    ans.append(correct[i] - piece[i])

print(*ans)
