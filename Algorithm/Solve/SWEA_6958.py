t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    a = [sum(list(map(int, input().split()))) for _ in range(n)]

    print(f"#{i}", a.count(max(a)), max(a))