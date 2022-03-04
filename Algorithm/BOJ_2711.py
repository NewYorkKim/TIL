t = int(input())

for i in range(t):
    a, b = input().split()
    print(b[0:int(a)-1]+b[int(a):])