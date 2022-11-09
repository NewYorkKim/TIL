n, m, k = map(int, input().split())
# cnt = 0

for i in range(k):
    if n >= m * 2:
        n -= 1
    else:
        m -= 1  

# while True:
#     if n >= 2 and m >= 1:
#         cnt += 1
#         n -= 2
#         m -= 1
#     else:
#         break

# print(cnt)
print(min(n//2, m))