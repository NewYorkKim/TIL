# 이진 탐색 알고리즘

> 2022/11/16

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`binary search` `algorithm` `python`



## 이진 탐색 알고리즘

- 순차 탐색: 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인**하는 방법

- 이진 탐색: 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법

    - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정



![이진탐색 동작 예시](https://t1.daumcdn.net/cfile/tistory/233C703B577E34840E)



### 이진 탐색의 시간 복잡도

-단계마다 탐색 범위를 2로 나누는 것과 동일하므로 **연산 횟수는 log₂N에 비례**

- 예를 들어 초기 데이터 개수가 32개일 때, 이상적으로 1단계를 거치면 16개가량의 데이터만 남음

    - 2단계를 거치면 8개가량의 데이터만 남음

    - 3단계를 거치면 4개가량의 데이터만 남음

- 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 **O(logN)**을 보장



### 이진 탐색 소스코드

- 재귀적 구현 
    ```python
    def binary_search(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, target, start, mid - 1)
        else:
            return bainary_search(array, target, mid + 1, end)

    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, n - 1)
    if result = None:
        print('원소가 존재하지 않습니다.')
    else:
        print(result + 1)
    ```



- 반복문 구현

    ```python
    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return None

    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0 , n - 1)
    if result == None:
        print('원소가 존재하지 않습니다.')
    else:
        print(result + 1)
    ```



### 이진 탐색 라이브러리

- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환

- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```

- 값이 특정 범위에 속하는 데이터 개수 구하기
    
    ```python
    from bisect import bisect_left, bisect_right

    def count_by_range(a, left_value, right_value):
        right_index = bisect_right(a, right_value)
        left_index = bisect_left(a, left_value)
        return right_index - left_index

    a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

    print(count_by_range(a, 4, 4))
    print(count_by_range(a, -1, 3))
    ```



### 파라메트릭 서치 (Parametric Search)

- **파라메트릭 서치** <U>최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법</U>

    - 예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제

- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **이진 탐색을 이용하여 해결**할 수 있음



### Python 구현 예제

```python
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
```

```python
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x= map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)
```



## 실습

- [백준 1920번](https://www.acmicpc.net/problem/1920) `success`
- [백준 10816번](https://www.acmicpc.net/problem/10816) `success`
