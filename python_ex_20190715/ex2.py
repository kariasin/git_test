class Node:
    head = None
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
def add(data):
    node = Node.head

    while node:
        prev = node
        node = node.next

    prev.next = Node(data)
    prev.next.prev = prev

Node.head = Node(0)
print(Node.head.data)
for data in range(1,10):
    add(data)
print(Node.head.data)