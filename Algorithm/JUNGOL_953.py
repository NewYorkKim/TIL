# record = input().split()
# foul = dict()

# for name in record:
#     foul[name] = record.count(name)

# least = min(foul.values())

# # print(*[name for name, time in foul.items() if time == least], least, sep='\n')

# print(*[name for name in foul if foul[name] == least], least, sep='\n')

record = input().split()
foul = dict()

for name in record:
    foul[name] = record.count(name)
for name in record:
    if name in foul:
        foul[name] += 1
    else:
        foul[name] = 1

least = min(foul.values())

print(*[name for name in foul if foul[name] == least], least, sep='\n')