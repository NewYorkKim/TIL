n = int(input())
seq = [0] * (n + 1)

for i in range(n+1):
    if i == 0:
        seq[i] = 1
    else:
        for j in range(i):
            seq[i] += seq[j] * seq[i-(j+1)]

print(seq[n])