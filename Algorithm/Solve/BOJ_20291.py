n = int(input())
files = [input().split(".")[1] for _ in range(n)]
file_dict = {}

for file in files:
    if file not in file_dict:
        file_dict[file] = 1
    else:
        file_dict[file] += 1

file_dict = sorted(list(file_dict.items()), key=lambda x: x[0])

for ex in file_dict:
    print(ex[0], ex[1])