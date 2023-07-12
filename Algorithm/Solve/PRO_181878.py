def solution(myString, pat):
    newString = myString.lower()
    newPat = pat.lower()
    
    if newPat in newString:
        return 1
    else:
        return 0