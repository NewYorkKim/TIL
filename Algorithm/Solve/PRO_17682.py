import re

def solution(dartResult):
    tmp = [0] * 3
    
    darts = re.findall(r"([0-9]+)([SDT])([*#]?)", dartResult)
    
    for i, (num, bon, opt) in enumerate(darts):
        tmp[i] = int(num)
        
        if bon == "D":
            tmp[i] **= 2
        elif bon == "T":
            tmp[i] **= 3
            
        if opt == "#":
            tmp[i] *= -1
        elif opt == "*":
            if i == 0:
                tmp[i] *= 2
            else:
                tmp[i] *= 2
                tmp[i-1] *= 2

    return sum(tmp)