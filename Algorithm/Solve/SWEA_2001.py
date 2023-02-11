t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]

    max = 0
    for x in range(n-m+1):
            for y in range(n-m+1): 
                tmp = []
                for line in fly[y:y+m]:
                    tmp += line[x:x+m]
                cnt = sum(tmp)
                print(tmp)
                if cnt > max:
                    max = cnt
    
    print(f"#{i}", max)
