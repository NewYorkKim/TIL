import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def cut(papers):
    global whites, blues

    l = len(papers)
    size = l ** 2

    temp = 0 
    for rows in papers:
        temp += sum(row for row in rows)
    if temp == 0 or temp == size:
        if papers[0][0]:
            blues += 1
        else:
            whites += 1
    else:
        cut([paper[: l // 2] for paper in papers[: l // 2]])
        cut([paper[: l // 2] for paper in papers[l // 2: ]])
        cut([paper[l // 2: ] for paper in papers[: l // 2]])
        cut([paper[l // 2: ] for paper in papers[l // 2: ]])

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
whites, blues = 0, 0

cut(papers)
print(whites)
print(blues)