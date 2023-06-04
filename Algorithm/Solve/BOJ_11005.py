n, b = map(int, input().split())
result = ""

while n > 0:
    tmp = n % b
    if tmp >= 10:
        tmp = chr(55 + tmp)
    result += str(tmp)
    n //= b

print(result[::-1])