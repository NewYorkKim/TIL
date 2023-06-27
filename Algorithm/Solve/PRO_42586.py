from math import ceil

def solution(progresses, speeds):
    remains = [ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    answer = []
    tmp, cnt = 0, 0
    
    for remain in remains:
        if tmp < remain:
            if cnt > 0:
                answer.append(cnt)
            tmp = remain
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    
    return answer