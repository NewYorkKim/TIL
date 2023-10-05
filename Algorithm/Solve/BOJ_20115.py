n = int(input())
drinks = sorted(list(map(float, input().split())), reverse=True)
total = drinks[0]
remains = [drink / 2 for drink in drinks[1:]]
total += sum(remains)

print(total)