n = int(input())
seq = [0] * n

for i in range(n):
    if (i == 0) or (i==1) or (i==2):
        seq[i] = 1
    else:
        seq[i] = seq[i-1] + seq[i-3]

print(seq[n-1])