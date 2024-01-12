def solution(n, computers):
    answer = 0
    
    que = []
    visited = []
    
    for i in range(n):
        if i not in visited:
            que.append(i)
            answer += 1
            
            while que:
                now = que.pop()
                for j in range(n):
                    if computers[now][j] == 1 and j not in visited:
                        visited.append(j)
                        que.append(j)
    return answer