import sys
input = sys.stdin.readline

# s = input()
# m = int(input())
# j = len(s)

# for i in range(m):
#     command = list(input().split())
#     if command[0] == "L":
#         if j != 0:
#             j -= 1
#     elif command[0] == "D":
#         if j != len(s):
#             j += 1
#     elif command[0] == "B":
#         if j != 0:
#             s = s[:j-1] + s[j:]
#                 j -= 1
#     elif command[0] == "P":
#         s = s[:j] + command[1] + s[j:]
#         if j != len(s):
#             j += 1

# print(s)

class Node:
    def __init__(self, val):
        self.val = val
        self.head = None
        self.next = None
        self.nodeCount = 0
    
    def getNode(self, cursor):
        i = 1
        crnt = self.head
        while i < cursor + 1:
            crnt = crnt.next 
            i += 1
        
        return crnt
    
    def deleteLeft(self, cursor):
        if cursor == 1:
            after = self.getNode(cursor)
            self.head = after
        else:
            before = self.getNode(cursor-2)
            after = before.next.next
            before.next = after
        self.nodeCount -= 1

    def appendLeft(self, cursor, new):
        new = Node(new)
        if cursor == 0:
            after = self.head
            self.head = new
        else:
            before = self.getNode(cursor-1)
            after = before.next
            before.next = new
        new.next = after
        self.nodeCount += 1

s = input()
m = int(input())
cursor = len(s)

for i in range(len(s)):
    if i == 0:
        node = Node(s[i])
        node.head = node
        tmp = node
    else:
        new_node = Node(s[i])
        tmp.next = new_node
        tmp = new_node
    node.nodeCount += 1

for i in range(m):
    command = list(input().split())
    if command[0] == "L":
        if cursor != 0:
            cursor -= 1
    elif command[0] == "D":
        if cursor != node.nodeCount:
            cursor += 1
    elif command[0] == "B":
        if cursor != 0:
            node.deleteLeft(cursor)
            cursor -= 1
    elif command[0] == "P":
        node.appendLeft(cursor, command[1])
        cursor += 1

for i in range(node.nodeCount):
    print(node.getNode(i).val, end="")