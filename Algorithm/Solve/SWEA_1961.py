def n90(matrix, n):
    result = []
    for x in range(n):
        tmp = ''
        for y in range(n-1, -1, -1):
            tmp += str(matrix[y][x])
        result.append(tmp)
    return result

def n180(matrix, n):
    result = []
    for x in range(n-1, -1, -1):
        tmp = ''
        for y in range(n-1, -1, -1):
            tmp += str(matrix[x][y])
        result.append(tmp)
    return result

def n270(matrix, n):
    result = []
    for x in range(n-1, -1, -1):
        tmp = ''
        for y in range(n):
            tmp += str(matrix[y][x])
        result.append(tmp)
    return result

t = int(input())

for i in range(1, t+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{i}')
    for e90, e180, e270 in zip(n90(matrix, n), n180(matrix, n), n270(matrix, n)):
        print(e90, e180, e270)



        

