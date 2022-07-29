def prime_list(n):
    m = 2 * n
    sieve = [True] * (m + 1)

    k = int(m ** 0.5)
    for i in range(2, k + 1):
        if sieve[i] == True:           
            for j in range(i+i, m + 1, i): 
                sieve[j] = False

    return len([i for i in range(2, m + 1) if sieve[i] == True and i > n])  
    
while True:
    n = int(input())
    if n == 0:
        break
    print(prime_list(n))



            
