class Solution:
    def tribonacci(self, n: int) -> int:
        fibo = [0] * (n + 3)
        fibo[1] = 1
        fibo[2] = 1

        if n <= 2:
            return fibo[n]
        
        for i in range(3, n+1):
            fibo[i] = fibo[i-1] + fibo[i-2] + fibo[i-3]

        return fibo[n]