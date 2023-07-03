def solution(arr):
    answer = []
    
    for a in arr:
        if (a >= 50):
            if (a % 2 == 0):
                a //= 2
        else:
            if (a % 2 != 0):
                a *= 2
        answer.append(a)
        
    return answer