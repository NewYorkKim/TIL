def solution(s):
    s = list(s)
    tmp = []
    # answer = True
    
    for x in s:
        if x == "(":
            tmp.append(x)
            
        else:
            try:
                tmp.pop()
            except:
                return False
#     flag = 0
    
#     for i in range(len(s)):
#         if i == 0:
#             if len(s) % 2 != 0:
#                 answer = False
#                 break
#             if s[i] == ")":
#                 answer = False
#                 break

#         if s[i] == "(":
#             flag += 1
#         if (flag > 0) and (s[i] == ")"):
#             flag -= 1

#     if flag > 0:
#         answer = False
    
#    return answer
        
    return len(tmp) == 0