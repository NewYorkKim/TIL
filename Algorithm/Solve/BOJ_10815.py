n = int(input())
n_cards = set(map(int, input().split()))

m = int(input())
m_cards = list(map(int, input().split()))

result = []

for card in m_cards:
    if card in n_cards:
        result.append(1)
    else:
        result.append(0)

print(*result)