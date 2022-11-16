n = int(input())

result = 0
for i in range(n//2, n+1):
    if i == n + 1:
        break
    num = i + sum(list(map(int, str(i))))
    if num == n:
        result = i
        break

print(result)
