# 정렬 알고리즘 비교

> 2022/06/23

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`sorting` `algorithm` `python`



## 정렬 알고리즘 비교

- 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장하도록 설계되어 있음



| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 | 특징                                                         |
| ------------- | ---------------- | ----------- | ------------------------------------------------------------ |
| 선택 정렬     | O(N²)            | O(N)        | 아이디어가 매우 간단                                         |
| 삽입 정렬     | O(N²)            | O(N)        | 데이터가 거의 정렬되어 있을 때는 가장 빠름                   |
| 퀵 정렬       | O(NlogN)         | O(N)        | 대부분의 경우에 가장 적합하며, 충분히 빠름                   |
| 계수 정렬     | O(N + K)         | O(N + K)    | 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작 |



### 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교

```python
from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))
    
start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
end_time = time.time()
print("선택 정렬 성능 측정:", end_time - start_time)

array = []
for _ in range(10000):
    array.append(randint(1, 100))
    
start_time = time.time()

array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)
```



## 실습

### 두 배열의 원소 교체

```python
n, k = map(int, input().split())
a = list(map(int, input()))
b = list(map(int, input()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
        
print(sum(a))
```

