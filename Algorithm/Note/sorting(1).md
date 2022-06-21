# 선택 정렬과 삽입 정렬

> 2022/06/21

`sorting` `algorithm` `python`



## 정렬 알고리즘

- **정렬**: 데이터를 특정한 기준에 따라 순서대로 나열
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용



## 선택 정렬

- 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복**



![img](https://velog.velcdn.com/images%2Fdongchyeon%2Fpost%2F4bbd7459-04bb-4c39-b9e9-2bbf03d3b271%2F%EC%84%A0%ED%83%9D%EC%A0%95%EB%A0%AC%20%EC%84%A4%EB%AA%851.png)

##### Python 구현 예제

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i 
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)
```



##### 시간 복잡도

- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
- 구현 방식에 따라 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같음
- N + (N - 1) + (N - 2) + ... + 2
- 이는 (N² + N - 2) / 2 로 표현할 수 있는데, 빅오 표기법에 따라서 **O(N²)**이라고 작성함



## 삽입 정렬

- 처리되지 않은 데이터를 하나씩 골라 **적절한 위치에 삽입**
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작



![img](https://velog.velcdn.com/images%2Fdongchyeon%2Fpost%2F8a635e87-199f-4bd9-8e64-47b04908120d%2F%EC%82%BD%EC%9E%85%20%EC%A0%95%EB%A0%AC%20%EC%84%A4%EB%AA%851.png)

##### Python 구현 예제

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
```



##### 시간 복잡도

- 삽입 정렬의 시간 복잡도는 **O(N²)**이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용
- 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
  - 최선의 경우 **O(N)**의 시간 복잡도를 가짐
  - 이미 정렬되어 있는 상태에서 다시 삽입 정렬을 수행한다면? ➡ **O(N)**