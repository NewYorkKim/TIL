n = int(input())
a_array = sorted(list(map(int, input().split())))
b_array = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(n):
    result += a_array[i] * b_array[i]

print(result)