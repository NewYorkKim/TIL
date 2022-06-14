start = int(input())
final = []

for i in range(start // 2, start + 1):
    result = [start, i]
    while True:
        new = result[-2] - result[-1]
        if new < 0:
            break
        result.append(new)
        if len(final) < len(result):
            final = result

print(len(final))
print(*final)
    


