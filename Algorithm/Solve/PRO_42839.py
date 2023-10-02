from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    answer = set()
    for i in range(1, len(numbers)+1):
        pers = permutations(numbers, i)
        for per in pers:
            tmp = int("".join(per))
            flag = True
            if tmp > 1:
                for j in range(2, tmp):
                    if tmp % j == 0:
                        flag = False
                        break
                if flag == True:
                    answer.add(tmp)
    return len(answer)