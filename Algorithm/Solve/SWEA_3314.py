t = int(input())

for i in range(1, t+1):
    scores = list(map(int, input().split()))
    
    for j in range(len(scores)):
        if scores[j] < 40:
            scores[j] = 40

    avg = sum(scores) // len(scores)
    print(f"#{i}", avg)