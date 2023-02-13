t = int(input())

for i in range(1, t+1):
    x = input()
    result = len(set(x))
    print(f"#{i}", result)