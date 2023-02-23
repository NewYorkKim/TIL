for t in range(1, 11):
    n = int(input())
    plain = list(input().split())
    m = int(input())
    comm = list(input().split())
    
    ins, tmp = [], []
    for i in range(len(comm)):
        if comm[i] in ['I', 'D', 'A']:
            if i != 0:
                ins.append(tmp)
            tmp = []
        tmp.append(comm[i]) 
        if i == len(comm)-1:
            ins.append(tmp)
    
    for j in range(m):
        if ins[j][0] == 'I':
            x = int(ins[j][1])
            y = int(ins[j][2])
            for k in range(y):
                plain.insert(x+k, ins[j][3+k])
        if ins[j][0] == 'D':
            x = int(ins[j][1])
            y = int(ins[j][2])
            for k in range(y):
                del plain[x+k]
        if ins[j] == 'A':
            y = int(ins[j][1])
            for k in range(y):
                plain.append(ins[j][2+k])
            
    print(f"#{t}", *plain[:10])
