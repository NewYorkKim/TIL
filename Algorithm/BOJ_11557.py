t = int(input())

for i in range(t):
    n = int(input())
    univ = {}
    for j in range(n):
        alcohol = input().split()
        univ[alcohol[0]] = int(alcohol[1])
    print(*[key for key, value in univ.items() if value == max(univ.values())])