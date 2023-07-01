def solution(number, n, m):
    answer = (number % n == 0) & (number % m == 0)
    
    return +answer