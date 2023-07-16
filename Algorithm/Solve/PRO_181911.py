def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(my_strings)):
        idx1, idx2 = parts[i][0], parts[i][1]
        string = my_strings[i][idx1: idx2+1]
        answer += string
        
    return answer