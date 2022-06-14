# 스택과 큐

> 2022/06/24 ~ ing

`datastructure` `algorithm` `python`



## 스택 자료구조

- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- __입구와 출구가 동일한 형태__



![img](https://velog.velcdn.com/images%2F717lumos%2Fpost%2F090765d9-dce1-4e73-a4ff-a855a8fbc497%2F%EA%B7%B8%EB%A6%BC9.png)



##### Python 구현 예제

```python
stack = []

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)  # 최하단 원소부터 출력
```



## 큐 자료구조

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- __입구와 출구가 모두 뚫려 있는 터널과 같은 형태__



![img](https://blog.kakaocdn.net/dn/eanvLg/btq3mO4both/LHk16XqBRdK3yPUaIJyd8k/img.png)



##### Python 구현 예제

```python
from collections import deque

queue = deque()

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소부터 
```

- list ➡ 시간 복잡도 ↑



## 실습

##### 스택 자료구조

- [백준 10828번](https://www.acmicpc.net/problem/10828) `success`

- [백준 10773번](https://www.acmicpc.net/problem/10773) `success`

- [백준 9012번](https://www.acmicpc.net/problem/9012)

- [백준 4949번](https://www.acmicpc.net/problem/4949)

- [백준 1874번](https://www.acmicpc.net/problem/1874)

- [백준 17298](https://www.acmicpc.net/problem/17298)



##### 큐 자료구조

- [백준 18258번](https://www.acmicpc.net/problem/18258) `success`

- [백준 2164번](https://www.acmicpc.net/problem/2164) `success`

- [백준 11866번](https://www.acmicpc.net/problem/11866) `success`

- [백준 1966번](https://www.acmicpc.net/problem/1966) `success`

  



