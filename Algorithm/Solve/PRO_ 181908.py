def solution(my_string, is_suffix):
    suffixes = []
    
    for i in range(len(my_string)):
        suffix = my_string[i:]
        suffixes.append(suffix)
        
    if is_suffix in suffixes:
        answer = 1
    else:
        answer = 0
        
    return answer