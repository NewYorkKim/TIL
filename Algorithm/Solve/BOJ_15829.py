l = int(input())
letters = input()

result = 0
for i in range(len(letters)):
    num = (ord(letters[i]) % 96) * (31**i)
    result += num

print(result % 1234567891)