n, m = map(int, input().split())
board = [input() for _ in range(n)]
count = []

for i in range(n-7):
    for j in range(m-7):
        cnt_b = 0
        cnt_w = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        cnt_w += 1
                    if board[a][b] != 'B':
                        cnt_b += 1
                else:
                    if board[a][b] != 'B':
                        cnt_w += 1
                    if board[a][b] != 'W':
                        cnt_b += 1
        count.append(min(cnt_b, cnt_w))

print(min(count))