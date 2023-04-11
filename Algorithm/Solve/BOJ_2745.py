n, b = input().split()
n = n[::-1]
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = 0

for i in range(len(n)):
    num += number.index(n[i]) * (int(b) ** i)

print(num)