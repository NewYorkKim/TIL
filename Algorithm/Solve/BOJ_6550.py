def solution(s, t):
    for i in t:
        if i == s[0]:
            s = s[1:]
        if len(s) == 0:
            return "Yes"
    return "No"
            
while True:
    try: 
        s, t = input().split()
        result = solution(s, t)
        print(result)
    except:
        break
            
