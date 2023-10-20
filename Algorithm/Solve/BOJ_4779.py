import sys
input = sys.stdin.readline

def cantor(arr):
    if len(arr) == 1:
        return arr
    
    mid = (len(arr) + 1) // 3

    left = cantor(arr[:mid])
    right = cantor(arr[mid * 2:])

    middle = [" "] * mid
    
    return left + middle + right

while True:
    try:
        n = int(input())
        arr = ["-"] * (3 ** n)
        print("".join(cantor(arr)))
    except:
        break