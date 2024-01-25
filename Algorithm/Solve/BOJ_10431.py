import sys
input = sys.stdin.readline

p = int(input())

for t in range(1, p+1):
    heights = list(map(int, input().split()))[1:]
    cnt = 0

    for i in range(1, len(heights)):
        for j in range(i):
            if heights[i] < heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                cnt += 1
    
    print(t, cnt)