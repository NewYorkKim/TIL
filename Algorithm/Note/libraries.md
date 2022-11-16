# 라이브러리

> 2022/11/03

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`library` `algorithm` `python`



## 실전에서 유용한 표준 라이브러리

- **내장 함수**: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공
    - 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능을 포함
    - sum, min, max, eval, sorted
- **itertools**: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공
    - 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용
    - permutations, combinations
- **heapq**: 힙(Heap) 자료구조 제공
    - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
- **bisect**: 이진 탐색(Binary Search) 기능 제공
- **collections**: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
- **math**: 필수적인 수학적 기능을 제공
    - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수 포함
    - factorial, sqrt, gcd, sin, cos, tan, pi



## 순열과 조합

- 모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 효과적으로 사용해야 할까?
- **순열**: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
    - {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우: 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
- **조합**: 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
    - {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우: 'AB', 'AC', 'BC'



### Python 구현 예제

```python
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)
```

```python
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)
```

```python
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
print(result)
```

```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)
```



## Counter

- 파이썬 collections 라이브러리의 **Counter**는 등장 횟수를 세는 기능을 제공
- 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 <U>내부의 원소가 몇 번씩 등장했는지</U>를 알려줌



### Python 구현 예제

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))
```



## 최대 공약수와 최소 공배수

- 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수 이용



### Python 구현 예제

```python
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14))
print(lcm(21, 14))
```