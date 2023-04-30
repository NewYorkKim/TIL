# 재귀 함수

> 2022/11/03

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`function` `algorithm` `python`



## 재귀 함수

- **재귀 함수(Recursive Function)**란 <U>자기 자신을 다시 호출하는 함수</U>를 의미
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
    - **종료 조건**을 포함한 재귀 함수 예시
    ```python
    def recursive_function(i):
        if i == 100:
            return 
        print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
        recursive_function(i + 1)
        print(i, '번째 재귀함수를 종료합니다,')
        
    recursive_function(1)
    ```
- <U>재귀 함수는 반복문을 이용하요 동일한 기능을 구현</U>할 수 있음
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
    - 그래서 스택을 사용해야 할 때 구현상 **스택 라이브러리 대신에 재귀 함수를 이용**하는 경우가 많음



### Python 구현 예제

```python
def factorial_iterative(n):
    result = 1
    for i in range(i, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
```

```python
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192, 162))
```