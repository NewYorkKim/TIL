def side(puzzle, n, k):
    cnt = 0
    for x in range(n):
        tmp = 0
        line = ''.join(puzzle[x])
        for y in line:
            if y == '1':
                tmp += 1
            else:
                if tmp == k:
                    cnt += 1
                tmp = 0
        if tmp == k:
            cnt += 1
    
    return cnt

def updown(puzzle, k):
    cnt = 0
    for e in zip(*puzzle):
        tmp = 0
        line = ''.join(list(e))
        for y in line:
            if y == '1':
                tmp += 1
            else:
                if tmp == k:
                    cnt += 1
                tmp = 0
        if tmp == k:
            cnt += 1

    return cnt
            
t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [input().split() for _ in range(n)]

    result = side(puzzle, n, k) + updown(puzzle, k)

    print(f"#{i}", result)

    
