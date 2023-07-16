def solution(myString):
    newString = myString.split("x")
    answer = [len(x) for x in newString]
            
    return answer