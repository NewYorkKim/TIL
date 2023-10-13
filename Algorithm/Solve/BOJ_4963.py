import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    global tmp
    tmp += 1
    
    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    dy = [1, -1, 1, -1, -1, 1, 0, 0]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < w and 0 <= ny < h:
            if geo[ny][nx] == 1:
                geo[ny][nx] = 0
                dfs(nx, ny)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    geo = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    for y in range(h):
        for x in range(w):
            if geo[y][x] != 0:
                tmp = 0
                geo[y][x] = 0
                dfs(x, y)
    
                if tmp > 0:
                    count += 1

    print(count)