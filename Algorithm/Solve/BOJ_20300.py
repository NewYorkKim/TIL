n = int(input())
degrees = sorted(list(map(int, input().split())))
last = degrees[-1]

for i in range(n//2):
    if n % 2 == 0:
        total = degrees[i] + degrees[n-1-i]
    else:
        total = degrees[i] + degrees[n-2-i]
    if total > last:
        last = total

print(last)