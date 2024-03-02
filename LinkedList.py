import config

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertAtFront(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        while self.length > MAX_STANCE_MEMORY:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
            self.length -= 1
    