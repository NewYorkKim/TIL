lines = []

while True:
    line = input()
    if line == 'END':
        break
    lines.append(line[::-1]) 

for line in lines:
    print(line)