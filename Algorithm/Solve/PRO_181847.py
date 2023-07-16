def solution(n_str):
    flag = False
    answer = ''
    
    for n in n_str:
        if flag == False:
            if n == "0":
                continue
            else:
                answer += n
                flag = True
        else:
            answer += n
            
    return answer