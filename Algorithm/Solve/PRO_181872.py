def solution(myString, pat):
    idx = myString.rfind(pat) + len(pat)
    answer = myString[:idx]
    
    return answer