n = int(input())

for i in range(2*n-1):
    if i <= n-1:
        print(" " * (n-(i+1)), end="")
        print("*" * (i*2+1))
    else:
        print(" " * (i-n+1), end="")
        print("*" * ((2*n-(i-n+1)*2)-1))