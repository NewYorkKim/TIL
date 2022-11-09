n = int(input())
time = sorted(list(map(int, input().split())))
total = 0

for i in range(len(time)):
    total += sum(time[:i+1])

print(total)