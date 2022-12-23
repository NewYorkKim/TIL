t = int(input())

for i in range(1, t+1):
    numbers = [j if j % 2 != 0 else -j for j in range(1, int(input())+1)]
    print(f'#{i}', sum(numbers))