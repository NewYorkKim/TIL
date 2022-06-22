# 퀵 정렬과 계수 정렬

> 2022/06/22

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`sorting` `algorithm` `python`



## 퀵 정렬

- 기준 데이터를 설정하고 그 **기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 **첫 번째 데이터를 기준 데이터(Pivot)로 설정**
  - 분할(Divide): 피벗을 기준으로 데이터 묶음을 나누는 작업



![img](https://miro.medium.com/max/1220/1*c8FT6a4d8bdZMxqYOxPL9A.png)



##### 퀵 정렬이 빠른 이유: 직관적인 이해

- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있음
  - 너비 X 높이 = N x logN = NlogN



##### 시간 복잡도

- 퀵 정렬은 평균의 경우 **O(NlogN)**의 시간 복잡도를 가짐
- 하지만 최악의 경우 **O(N²)**의 시간 복잡도를 가짐
  - 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행한다면? ➡ **O(N²)**



##### Python 구현 예제

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
	quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) - 1)
print(array)
            
```

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```



## 계수 정렬

- 특정한 조건이 부합할 때만 사용할 수 있지만 **매우 빠르게 동작하는** 정렬 알고리즘
  - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 **O(N + K)**를 보장



![계수 정렬(Count Sort) - fora22/CodingTest Wiki](https://user-images.githubusercontent.com/48875566/104679966-283d0100-5732-11eb-88a8-d31c01aadc7d.png)



##### Python 구현 예제

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```



##### 시간 복잡도

- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 **O(N + K)**
- 계수 정렬은 때에 따라서 심각한 비효율성 초래
  - 데이터가 0과 999,999로 단 2개만 존재하는 경우
- 계수 정렬은 **동일한 값을 가지는 데이터가 여러 개 등장할 때** 효과적
  - 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적





## 실습

##### 계수 정렬

- [백준 10989번](https://www.acmicpc.net/problem/10989) `success`