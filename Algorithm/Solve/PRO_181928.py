def solution(num_list):
    even, odd = [], []
    
    for num in num_list:
        if num % 2 == 0:
            even.append(str(num))
        else:
            odd.append(str(num))
            
    even = int("".join(even))
    odd = int("".join(odd))
    
    answer = even + odd
    
    return answer