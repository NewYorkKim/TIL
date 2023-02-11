t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())

    start = (0 + a) % 24
    result = (start + b) % 24

    print(f"#{i}", result)