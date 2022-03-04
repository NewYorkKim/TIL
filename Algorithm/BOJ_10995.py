# n = int(input())

# for i in range(n):
#     if i % 2 == 0: print('* '*i)
#     else: print(' '+'* '*i)

n = int(input())

for i in range(n):
    print(' '*(i%2)+'* '*n)