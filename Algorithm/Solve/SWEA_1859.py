t = int(input())

for i in range(1, t+1):
    n = int(input())
    prices = list(map(int, input().split()))
    result, flag = 0, 0

    for j in range(n-1, -1, -1):
        if j == n-1:
            flag = prices[j]
        elif prices[j] <= flag:
            result += flag - prices[j]
        else:
            flag = prices[j]

    print(f"#{i}", result)