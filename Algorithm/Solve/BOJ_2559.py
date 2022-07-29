n, k = map(int, input().split())
temperature = list(map(int, input().split()))

start = sum(temperature[:k])
sub_temperature = temperature[k:]
result = [start]

for i in range(n - k):
    new = start - temperature[i] + sub_temperature[i]
    result.append(new)
    start = new

print(max(result))