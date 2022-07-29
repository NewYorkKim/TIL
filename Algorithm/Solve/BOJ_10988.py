# a = input()
# cnt = 0

# for i in range(len(a)//2):
#     if a[i] == a[-(i+1)]:
#         cnt += 1
    
# if cnt == len(a)//2:
#     print(1)
# else:
#     print(0)

a = input()

print(+(a[::-1]==a))