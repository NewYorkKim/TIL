def solution(n, arr1, arr2):
    answer = []
    
    for line1, line2 in zip(arr1, arr2):
        line1 = str(format(line1, "b").zfill(n))
        line2 = str(format(line2, "b").zfill(n))
        tmp = ""
        
        for i in range(n):
            if line1[i] == "1" or line2[i] == "1":
                tmp += "#"
            else:
                tmp += " "
        
        answer.append(tmp)
        
    return answer