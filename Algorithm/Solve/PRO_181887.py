def solution(num_list):
    even = sum([num_list[i] for i in range(len(num_list)) if i % 2 != 0])
    odd = sum([num_list[i] for i in range(len(num_list)) if i % 2 == 0])
    
    answer = max(even, odd)
    
    return answer