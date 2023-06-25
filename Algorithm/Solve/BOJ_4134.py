from math import sqrt

t = int(input())

for _ in range(t):
    n = int(input())

    while True:
        flag = False

        if n < 2:
            print(2)
            break

        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                flag = True
                break
        
        if flag == True:
            n += 1
        else:
            print(n)
            break