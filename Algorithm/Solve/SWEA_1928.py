t = int(input())

table = {s: i for i, s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}

for i in range(1, t+1):
    string = input()
    binary = ''.join([bin(table[j])[2:].zfill(6) for j in string])
    text = ''.join([chr(int(binary[k:k+8], 2)) for k in range(0, len(binary), 8)])

    print(f'#{i}', text)



