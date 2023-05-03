a_number = list(map(int, input()))
b_number = list(map(int, input()))

score = []

for i in range(len(a_number)):
    score.append(a_number[i])
    score.append(b_number[i])

while len(score) > 2:
    tmp = [0] * (len(score) - 1)
    for i in range(len(tmp)):
        tmp[i] = (score[i] + score[i+1]) % 10
    score = tmp

for j in score:
    print(j, end='')