n = int(input())
fibo = [0] * (n+1)

for i in range(n+1):
    if (i == 0) or (i == 1):
        fibo[i] = i
    else:
        # 마지막에 나머지 연산을 하는 경우, list에 너무 큰 수가 많이 저장되어 메모리 초과 발생
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000007

print(fibo[n])