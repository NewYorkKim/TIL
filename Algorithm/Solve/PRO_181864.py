def solution(myString, pat):
    answer = 0
    newString = ""
    
    for string in myString:
        if string == "A":
            newString += "B"
        else:
            newString += "A"
            
    if pat in newString:
        answer = 1
    else:
        answer = 0
        
    return answer