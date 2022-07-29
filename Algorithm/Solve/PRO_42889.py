# import operator

def solution(N, stages):
    answer = []
    fail = dict()
    total = len(stages)
    
    for i in range(N):
        now = stages.count(i + 1)
        if total == 0:
            fail[i + 1] = 0
        else:
            fail[i + 1] = now / total
        total -= now
        
    # rank = sorted(fail.items(), key=operator.itemgetter(1), reverse=True)
    rank = sorted(fail.items(), key=lambda x : x[1], reverse=True)
    
    answer = list(zip(*rank))[0]
            
    return answer