r, c = map(int, input().split())
images = [list(map(int, input().split())) for _ in range(r)]
t = int(input())
filter = []

for i in range(r-2):
    for j in range(c-2):
        tmp = []
        for k in range(3):
            tmp.extend(images[i+k][j:j+3])
            
        tmp.sort()
        if tmp[4] >= t:
            filter.append(tmp[4])

print(len(filter))