def solution(arr):
    answer = []
    last = ""
    
    for a in arr:
        if a == last:
            continue
        else:
            answer.append(a)
            last = a
    
    return answer