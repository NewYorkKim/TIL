import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = str(bin(int(input()))[2:])[::-1]

    for i in range(len(n)):
        if n[i] == "1":
            print(i, end=" ")