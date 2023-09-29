def recursion(s, l, r):
    global n
    n += 1
    if l >= r: return (1)
    elif s[l] != s[r]: return (0)
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())

for _ in range(t):
    s = input()
    global n
    n = 0
    result = isPalindrome(s)
    print(result, n)
