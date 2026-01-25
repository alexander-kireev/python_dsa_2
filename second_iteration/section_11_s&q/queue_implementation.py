class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.front = new_node
        self.back = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)

        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.front is None:
            return None
        
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.back = None

        self.length -= 1
        return temp
    
