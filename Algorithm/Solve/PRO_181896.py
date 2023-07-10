def solution(num_list):
    answer = -1
    
    for idx in range(len(num_list)):
        if num_list[idx] < 0:
            answer = idx
            break
            
    return answer