def solution(priorities, location):
    answer = 1
    
    while len(priorities) > 0:
        priority = max(priorities)
        tmp = priorities.pop(0)
        
        if tmp == priority:
            if location == 0:
                return answer
            else:
                if location == 0:
                    location = len(priorities) - 1
                    answer += 1
                else:
                    location -= 1
                    answer += 1
        else:
            priorities.append(tmp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            
    return answer