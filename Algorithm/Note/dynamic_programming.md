# 다이나믹 프로그래밍

> 2023/04/30

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`dynamic programming` `algorithm` `python`

## 다이나믹 프로그래밍

- **메모리를 적절히 사용하여 수행 시간 효율성을 비약정으로 향상히키는 방법**
- 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 함
- 탑다운과 보텀업으로 구성
- **동적 계획법**
- 일반적인 프로그래밍 분야에서의 동적(Dynamic)이란?
    - 자료구조에서 동적 할당(Dynamic Allocation)은 **'프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'**
    - 반면에 다이나믹 프로그래밍에서 '다이나믹'은 **별다른 의미 없이 사용된 단어**

### 다이나믹 프로그래밍의 조건
1. **최적 부분 구조 (Optional Substructure)**
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결
2. **중복되는 부분 문제 (Overlapping Subproblem)**
    - 동일한 작은 문제를 반복적으로 해결

### 다이나믹 프로그래밍 vs. 분할 정복

- 다이나믹 프로그래밍과 분할 정복은 모두 **최적 부분 구조**를 가질 때 사용할 수 있음
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황
- 다이나믹 프로그래밍과 분할 정복의 차이점은 **부분 문제의 중복**
    - 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복
    - 분할 정복 문제에서는 동일한 문제가 반복적으로 계산되지 않음
- 분할 정복의 대표적인 예시인 퀵 정렬
    - 한 번 기준 원소(Pivot)가 자리를 변경해서 자리를 잡으면 그 기준 원소의 위치는 바뀌지 않음
    - 분할 이후에 해당 피벗을 다시 처리하는 부분 문제는 호출되지 않음

### 다이나믹 프로그래밍 문제에 접근하는 방법

- 주어진 문제가 **다이나믹 프로그래밍 유형임을 파악**하는 것이 중요
- 가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토
    - 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 다이나믹 프로그래밍을 고려
- 일단 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법을 사용
- <U>일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제</U>되는 경우가 많음

### Python 코드 예제: 개미 전사

```python
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
```

### Python 코드 예제: 1로 만들기

```python
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
```

### Python 코드 예제: 효율적인 화폐 구성

```python
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
```

### Python 코드 예제: 금광

```python
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index+m])
        index += m
    for j in range(1, m):
        for i in range(n):
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            if i == n - 1: left_down = 0
            else: left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
```

### Python 코드 예제: 병사 배치하기

```python
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))
```

## 피보나치 수열
- 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
- **점화식**이란 인접한 항들 사이의 관계식을 의미

![피보나치 수열 - 점화식](https://t1.daumcdn.net/cfile/tistory/9978EF3F5BDF062318)

- 배열이나 리스트를 애용해 표현

![피보나치 수열 - 트리](https://ko.javascript.info/task/fibonacci-numbers/fibonacci-recursion-tree.svg)

```python
# 피보나치 함수 (Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4)) # 3
```

### 피보나치 수열의 시간 복잡도 분석

- 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됨
- **중복되는 부분 문제**
- **시간 복잡도**
    - 세타 표기법: θ(1.618...ᴺ)
    - 빅오 표기법: O(2ᴺ)
- 빅오 표기법을 기준으로 f(30)을 계산하기 위해 약 10억가량의 연산을 수행해야 함

### 피보나치 수열의 효율적인 해법: 다이나믹 프로그래밍

- 다이나믹 프로그래밍의 사용 조건을 만족하는지 확인
    1. **최적 부분 구조**
    2. **중복되는 부분 문제**

### 메모이제이션 (Memoization)

- 다이나믹 프로그래밍을 구현하는 방법 중 하나
- <U>한 번 계산한 결과를 메모리 공간에 메모하는 기법</U>
    - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
    - **캐싱(Caching)**: 값을 기록해 놓음
- 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 **O(N)**

### 탑다운 vs. 보텀업

- 탑다운(메모이제이션) 방식은 **하향식**이라고도 하며 보텀업 방식은 **상향식**이라고도 함
- 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식
    - 결과 저장용 리스트는 **DP 테이블**이라고 부름
- 엄밀히 말하면 메모이제이션은 <U>이전에 계산된 결과를 일시적으로 기록해 놓은 넓은 개념을 의미</U>
    - 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아님
    - 한 번 게산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음

### 피보나치 수열: 탑다운 다이나믹 프로그래밍 (Python 구현 예제)
```python
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    retrun d[x]

print(fibo(99))
```

### 피보나치 수열: 보텀업 다이나믹 프로그래밍 (Python 코드 예제)
```python
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i-1] + d[i - 2]

print(d[n])
```

