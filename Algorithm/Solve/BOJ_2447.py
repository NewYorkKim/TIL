import sys
input = sys.stdin.readline

def stars(star):
    tmp = []

    for i in range(3 * len(star)):
        if i // len(star) == 1:
            tmp.append(star[i % len(star)] + " " * len(star) + star[i % len(star)])
        else:
            tmp.append(star[i % len(star)] * 3)
        
    return tmp

n = int(input())
star = ["***", "* *", "***"]
iter = 0

while n != 3:
    n = n // 3
    iter += 1

for i in range(iter):
    star = stars(star)

for i in star:
    print(i)
