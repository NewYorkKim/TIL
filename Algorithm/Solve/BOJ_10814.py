n = int(input())
members = [input() for _ in range(n)]
members = sorted(members, key=lambda x: int(x.split()[0]))

print(*members, sep="\n")