def side(puzzle, n, k):
    cnt = 0
    for x in range(n):
        line = ''.join(puzzle[x])

def updown(puzzle, k):
    cnt = 0
    for e in zip(*puzzle):
        line = ''.join(list(e))

t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [input().split() for _ in range(n)]

    # result = side(puzzle, n, clues) + updown(puzzle, clues)

    # print(f"#{i}", result)

    
