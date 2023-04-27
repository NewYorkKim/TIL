import sys
input = sys.stdin.readline

m = int(input())
s = []

for i in range(m):
    command = list(input().split())
    if len(command) > 1:
        x = int(command[1])

    if command[0] == 'add':
        if x not in s:
            s.append(x)
    elif command[0] == 'remove':
        if x in s:
            s.remove(x)
    elif command[0] == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.append(x)
    elif command[0] == 'all':
        s = [i+1 for i in range(20)]
    elif command[0] == 'empty':
        s = []