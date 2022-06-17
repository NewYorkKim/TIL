# 트리

> 2022/06/16

`data structure` `algorithm` `python`



## 트리

- __계층적인 구조__를 표현할 때 사용할 수 있는 자료구조
  - 루트 노드: 부모가 없는 최상위 노드
  - 단말 노드: 자식이 없는 노드
  - 크기: 트리에 포함된 모든 노드의 개수
  - 깊이: 루트 노드부터의 거리
  - 높이: 깊이 중 최댓값
  - 차수: 각 노드의 (자식 방향) 간선 개수
- 기본적으로 트리의 크기가 __N__일 때, 전체 간선의 개수는 __N-1__개



![img](https://velog.velcdn.com/images%2Fmuchogusto%2Fpost%2F7a926065-c1dd-4d07-9541-b7f386ce0d7c%2Fimage.png)



##### 이진 탐색 트리

- __이진 탐색__이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종
- 이진 탐색 트리의 특징: __왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드__
  - 부모 노드보다 왼쪽  자식 노드가 작음
  - 부모 노드보다 오른쪽 자식 노드가 큼



![이진탐색트리(Binary Search Tree) · ratsgo's blog](https://i.imgur.com/po0R4GB.png)



## 트리의 순회

- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법
  - 트리의 정보를 시각적으로 확인
- 대표적인 트리 순회 방법
  - __전위 순회__: 루트를 먼저 방문
  - __중위 순회__: 왼쪽 자식을 방문한 뒤에 루트를 방문
  - __후위 순회__: 오른쪽 자식을 방문한 뒤에 루트를 방문



##### Python 구현 예제

```python
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순회
def pre_order(node):
	print(node.data, end=' ')
    if node.left_node != None:
    	pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
            
# 중위 순회
def in_order(node):
	if node.left_node != None:
    	in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])
            
# 후위 순회
def post_order(node):
	if node.left_node != None:
    	post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')
        
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
```



## 실습

- [백준 11725번](https://www.acmicpc.net/problem/11725)
- [백준 1167번]()
- [백준 1967번]()
- [백준 1991번](https://www.acmicpc.net/problem/1991) `success`
- [백준 2263번]()
- [백준 5639번]()
- [백준 4803번]()