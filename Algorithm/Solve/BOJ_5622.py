dial = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
total = 0

for letter in input():
    time = sum([key for key, value in dial.items() if letter in value]) + 1
    total += time
    
print(total)