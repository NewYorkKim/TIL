import sys
input = sys.stdin.readline

def hanoi(n, start, dest, via):
    if n == 1:
        move.append((start, via))
    else:
        hanoi(n-1, start, via, dest)
        move.append((start, via))
        hanoi(n-1, dest, start, via)

n = int(input())
move = []

hanoi(n, 1, 2, 3)
print(len(move))

for i in move:
    print(i[0], i[1])