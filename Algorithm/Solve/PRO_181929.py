def solution(num_list):
    mul_n = 1
    
    for num in num_list:
        mul_n *= num
        
    sum_n = sum(num_list) ** 2
    
    answer = min(mul_n, sum_n) == mul_n
    
    return +answer