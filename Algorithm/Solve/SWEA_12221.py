t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    result = a * b
    if (a >= 10) or (b >= 10):
        result = -1
    print(f"#{i}", result)