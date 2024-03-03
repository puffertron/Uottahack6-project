import config

#Node class
class Node:
    def __init__(self, data):
        #data should be a list of strings
        self.data = data
        self.next = None
        self.prev = None
    
    #Get the data from node
    def getData(self):
        return self.data
    
    #Return the next pointer
    def getNext(self):
        #Error handling
        if next == None:
            return
        
        return next

#Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #Inserts a new node at the front of the list
    def insertAtFront(self, data):
        new_node = Node(data)
        #First node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        #Every other node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

        #Automatically delete the last node once the list has reached as certain size
        while self.length > config.MAX_STANCE_MEMORY:
            self.tail = self.tail.prev
            self.tail.next.prev = None
            self.tail.next = None
            self.length -= 1
    
    #Get the data from the node at the specified index
    def getAtIndex(self, index):
        #Error handling
        if index > self.length:
            return
        
        counter = 0
        it = self.head
        #Iterate through list to get object at index
        while counter <= index:
            it = it.next
            counter += 1

        return it

    #Return a pointer to the head
    def getHead(self):
        #Error handling
        if self.head == None:
            return
        
        return self.head


    
    
    