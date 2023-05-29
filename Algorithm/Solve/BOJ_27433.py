def recursion(n):
    if n <= 1:
        return 1
    return n * recursion(n-1)

n = int(input())
result = recursion(n)

print(result)