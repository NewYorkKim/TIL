n = int(input())
ropes = sorted([int(input()) for _ in range(n)], reverse=True)
weight = []

for i in range(len(ropes)):
    w = ropes[i] * (i+1)
    weight.append(w)

print(max(weight))