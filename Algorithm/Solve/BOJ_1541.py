row = input()
# isMinus = False

# for i in range(len(row)):
#     if row[i] == '-':
#         isMinus = True
#     elif row[i] == "+" and isMinus == True:
#         row = row[:i] + '-' + row[i+1:]
#     else:
#         num += row[i]
    
# print(eval(row))

result = 0
token = row.split('-')

for i in range(len(token)):
    for j in token[i].split('+'):
        if i == 0:
            result += int(j)
        else:
            result -= int(j)

print(result)