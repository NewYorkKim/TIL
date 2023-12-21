import sys
input = sys.stdin.readline

def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == x - i:
            return False
    return True

def queen(x, n):
    global count
    if x == n:
        count += 1
    else:
        for i in range(n):
            visited[x] = i
            if check(x):
                queen(x+1, n)
    

n = int(input())
visited = [0] * n
count = 0

queen(0, n)
print(count)