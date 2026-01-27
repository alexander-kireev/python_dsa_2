class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        return temp
    
    def print_stack(self):
        cur = self.top
        
        while cur is not None:
            print(cur.value)
            cur = cur.next
        
    def is_empty(self):
        return self.height == 0