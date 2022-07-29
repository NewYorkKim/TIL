# def check_sudoku(sudoku):
#     for row in sudoku:
#         if len(set(row)) < 9:
#             return False

#     for col in zip(*sudoku):
#         if len(set(col)) < 9:
#             return False
    
#     for k in range(0, 9, 3):
#         for l in range(0, 9, 3):
#             square = [sudoku[x][y] for x in range(k, k + 3) for y in range(l, l + 3)]
#             if len(set(square)) < 9:
#                 return False
#     return True

# n = int(input())

# for i in range(n):
#     if i > 0:
#         input()

#     sudoku = [list(map(int, input().split())) for j in range(9)]
   
#     print(f'Case {i + 1}:', 'CORRECT' if check_sudoku(sudoku) == True else 'INCORRECT')

def is_correct(sudoku):
    for line in sudoku:
        if len(set(line)) < 9: 
            return False
    return True


for t in range(1, int(input()) + 1):
    if t > 1:
        input()

    sudoku1 = [list(map(int, input().split())) for _ in range(9)]

    sudoku3 = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            line = [sudoku1[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            sudoku3.append(line)

    if is_correct(sudoku1) and is_correct(zip(*sudoku1)) and is_correct(sudoku3):
        print(f"Case {t}: CORRECT")
    else:
        print(f"Case {t}: INCORRECT")