t = int(input())

for i in range(t):
    line = input()
    max = sorted([line.count(x) for x in line if x != ' '], reverse=True)[0]
    candidate = set([y for y in line if (y != ' ') & (line.count(y) == max)])

    if len(candidate) == 1:
        print(*candidate)
    else:
        print("?")