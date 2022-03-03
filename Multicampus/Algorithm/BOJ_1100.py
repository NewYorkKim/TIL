# total = 0

# for i in range(8):
#     chess = list(input())
#     for j in range(8):
#         if i % 2 == 0 and j % 2 == 0:
#             total += 1 if chess[j] == 'F' else 0
#         if i % 2 != 0 and j % 2 != 0:
#             total += 1 if chess[j] == 'F' else 0
        
# print(total)

total = 0

for i in range(8):
    chess = input()
    total += chess[i%2::2].count('F')
        
print(total)
