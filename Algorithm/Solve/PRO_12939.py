def solution(s):
    s = list(map(int, s.split()))
    answer = f"{str(min(s))} {str(max(s))}"
    
    return answer