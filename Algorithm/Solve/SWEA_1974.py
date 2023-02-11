def side(puzzle):
    for line in puzzle:
        if len(set(line)) == 9:
            continue
        else:
            return False
    return True

def updown(puzzle):
    for line in zip(*puzzle):
        if len(set(line)) == 9:
            continue
        else:
            return False
    return True

def square(puzzle):
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            tmp = []
            for line in puzzle[y:y+3]:
                tmp += line[x:x+3]
            if len(set(tmp)) == 9:
                continue
            else:
                return False
    return True

t = int(input())

for i in range(1, t+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    square(puzzle)
    result = side(puzzle) and updown(puzzle) and square(puzzle)
    print(f"#{i}", +(result))