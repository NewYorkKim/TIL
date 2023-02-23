def check_side(puzzle, n):
    cnt = 0
    for line in puzzle:
        for x in range(8-n+1):
            if line[x:x+n] == line[x:x+n][::-1]:
                cnt += 1
    return cnt

def check_updown(puzzle, n):
    cnt = 0
    for line in zip(*puzzle):
        for x in range(8-n+1):
            if line[x:x+n] == line[x:x+n][::-1]:
                cnt += 1
    return cnt

for i in range(1, 11):
    n = int(input())
    puzzle = [input() for _ in range(8)]

    result = check_side(puzzle, n) + check_updown(puzzle, n)

    print(f"#{i}", result)