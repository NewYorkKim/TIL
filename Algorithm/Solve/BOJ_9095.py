t = int(input())

for _ in range(t):
    n = int(input())
    dp = [set()] * (n + 3)
    dp[0] = {'1'}
    dp[1] = {'11', '2'}
    dp[2] = {'111', '12', '21', '3'}

    if n > 3 :
        for i in range(3, n):
            tmp = set()
            for j in range(1, 4):
                num = str(j)
                for ele in dp[i-j]:
                    tmp.add(ele+num)
                    tmp.add(num+ele)
            dp[i] = tmp

    print(len(dp[n-1]))