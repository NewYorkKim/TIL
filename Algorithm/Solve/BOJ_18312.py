n, k = map(int, input().split())

total = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = f"{h:02d}:{m:02d}:{s:02d}"

            if str(k) in time:
                total += 1

print(total)

