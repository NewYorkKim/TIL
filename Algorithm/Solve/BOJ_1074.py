import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def recurse(x, y, n):
    global ans
    if x == r and y == c:
        print(ans)
        exit()

    if n == 1:
        ans += 1
        return 
    
    if not (x <= r <= x + n and y <= c < y + n):
        ans += n * n
        return
    
    recurse(x, y, n // 2)
    recurse(x, y + (n // 2), n // 2)
    recurse(x + (n // 2), y, n // 2)
    recurse(x + (n // 2), y + (n // 2), n // 2)


n, r, c = map(int, input().split())
ans = 0
recurse(0, 0, 2 ** n)