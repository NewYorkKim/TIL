# 그리디 & 구현

> 2022/11/03

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`greedy`  `implementation` `algorithm` `python`



## 그리디 알고리즘

- 그리디 알고리즘(탐욕법)은 **현재 상황에서 지금 당장 좋은 것만 고르는 방법**을 의미
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
- 그리디 해법은 그 정당성 분석이 중요
    - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토
- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많음
- 하지만 코딩 테스트에서의 대부분의 그리디 문제는 **탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론**할 수 있어야 풀리도록 출제



### Python 구현 예제

```python
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)
```

```python
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
```

```python
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
```

```python
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
```



## 구현(Implementation)

- 구현이란, **머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정**
- 흔히 알고리즘 대회에서 구현 유형의 문제란?
    - **풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제** 
- 구현 유형의 예시
    - 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
    - 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
    - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
    - 적절한 라이브러리를 찾아서 사용해야 하는 문제
- 일반적으로 알고리즘 문제에서의 2차원 공간은 **행렬(Matrix)**의 의미로 사용
- 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 **방향 벡터**가 자주 활용
    ```python
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    x, y = 2, 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print(nx, ny)
    ```



### Python 구현 예제

```python
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = x + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
```

```python
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
```

```python
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2,), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)
```

```python
data = intput()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
```



## 실습

### 그리디 알고리즘

- [백준 2839번](https://www.acmicpc.net/problem/2839) `success`

- [백준 1931번](https://www.acmicpc.net/problem/1931) `success`

- [백준 11047번](https://www.acmicpc.net/problem/11047) `success`

- [백준 2875번](https://www.acmicpc.net/problem/2875) `success`

- [백준 10610번](https://www.acmicpc.net/problem/10610) `success`

- [백준 1783번](https://www.acmicpc.net/problem/1783)

- [백준 11000번](https://www.acmicpc.net/problem/11000)

- [백준 11399번](https://www.acmicpc.net/problem/11399) `success`

- [백준 2217번](https://www.acmicpc.net/problem/2217) `success`

- [백준 13458번](https://www.acmicpc.net/problem/13458) `success`

- [백준 1946번](https://www.acmicpc.net/problem/1946) `success`

- [백준 4796번](https://www.acmicpc.net/problem/4796) `success`

- [백준 1541번](https://www.acmicpc.net/problem/1541) `success`

- [백준 12845번](https://www.acmicpc.net/problem/12845)

- [백준 2873번](https://www.acmicpc.net/problem/2873)

- [백준 1744번](https://www.acmicpc.net/problem/1744)

- [백준 1700번](https://www.acmicpc.net/problem/1700)

- [백준 1969번](https://www.acmicpc.net/problem/1969)