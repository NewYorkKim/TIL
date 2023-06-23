n = int(input())
result = []

for i in range(n):
    for j in range(n):
        if i != j:
            result.append((i, j))

print(len(result))