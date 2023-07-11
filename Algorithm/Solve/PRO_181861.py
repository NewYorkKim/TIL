def solution(arr):
    answer = []
    for a in arr:
        tmp = [a] * a
        answer.extend(tmp)
        
    return answer