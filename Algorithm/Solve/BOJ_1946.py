import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    result = n
    new = sorted([tuple(map(int, input().split())) for _ in range(n)])
    target = new[0][1]
    for i in range(1, n):
        if new[i][1] < target:
            target = new[i][1]
        else:
            result -= 1
    print(result)



   
    

