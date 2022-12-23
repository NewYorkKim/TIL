n = int(input())
km = list(map(int, input().split()))
gas = list(map(int, input().split()))
low = min(gas[:-1])
target = gas[0]
result = 0

for i in range(n-1):
    if gas[i] != low:
        if gas[i] < target:
            target = gas[i]
        result += km[i] * target
    else:
        result += sum(km[i:]) * gas[i]
        break

print(result)