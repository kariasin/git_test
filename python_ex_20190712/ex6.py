# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = ''
# def add(data):
#     node = head
#     while head.next:
#         node = head.next
#     node.next = Node(data)

# head = Node(10)
# add(11)

# print(head.data)
# print(head.next.data)


# node1 = Node(10)
# print(node1.data)

# 노드 클래스 만들기
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node5
node3.next = node4
node5.next = node3

node = node1
while node:
    print(node.data)
    node = node.next






