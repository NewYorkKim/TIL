# 우선순위 큐

> 2022/06/15

- source: [이것이 취업을 위한 코딩 테스트다 with 파이썬](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)

`data structure` `algorithm` `python`



## 우선순위 큐

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 데이터를 __우선순위에 따라__ 처리하고 싶을 때 사용



![자료구조_ch8_우선순위 큐 : 네이버 블로그](https://mblogthumb-phinf.pstatic.net/MjAxODExMjFfMjc1/MDAxNTQyNzgwNjUzNjA3.6X1oUq00atBXXbBa42J5xbVrVIdzwlMj1_PfmKOsKCcg.z2Aq12efaE1YU2NRAbqFcEJ45njRXYDQ_CUxGADZTBsg.PNG.kimbh666/image.png?type=w800)



- 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일 
  - 힙 정렬
  - 시간 복잡도: O(NlogN)



## 힙의 특징

- 완전 이진 트리 자료구조의 일종
- 힙에서는 항상 __루트 노드를 제거__
- 최소 힙
  - 루트 노드가 가장 작은 값을 가짐
  - 값이 작은 데이터가 우선적으로 제거
- 최대 힙
  - 루트 노드가 가장 큰 값을 가짐
  - 값이 큰 데이터가 우선적으로 제거



![img](https://velog.velcdn.com/images%2Fjaenny%2Fpost%2Ff4b21402-6df3-4cec-bb2a-429d06880c7a%2Fimg.png)



- 새로운 원소가 삽입되었을 때 __O(logN)__ 시간 복잡도로 힙 성질을 유지
- 원소가 제거되었을 때 __O(logN)__의 시간 복잡도로 힙 성질 유지
  - 가장 마지막 노드가 루트 노드의 위치에 오도록
  - 이후에 루트 노드에서부터 하향식으로 (더 작은 자식 노드로) Heapify()를 진행



### 완전 이진 트리

- 루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리



### 최소 힙 구성 함수: Min-Heapify()

- (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체



### Python 구현 예제

```python
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])
```



## 실습

- [백준 1927번](https://www.acmicpc.net/problem/1927) `success`

- [백준 11279번](https://www.acmicpc.net/problem/11279) `success`

- [백준 11286번](https://www.acmicpc.net/problem/11286) `success`

- [백준 1417번](https://www.acmicpc.net/problem/1417) `success`

- [백준 14235번](https://www.acmicpc.net/problem/14235) `success`

- [백준 15903번](https://www.acmicpc.net/problem/15903)

- [백준 2075번](https://www.acmicpc.net/problem/2075)

- [백준 1715번](https://www.acmicpc.net/problem/1715)

- [백준 1655번](https://www.acmicpc.net/problem/1655)

  