ans = -1
x, y = 0, 0

for i in range(9):
    grid = list(map(int, input().split()))
    tmp = max(grid)
    if tmp > ans:
        ans = tmp
        x, y = i+1, grid.index(tmp)+1

print(ans)
print(x, y)