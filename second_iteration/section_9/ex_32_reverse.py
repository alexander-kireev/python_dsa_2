class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_list(self):
        cur = self.head

        while cur is not None:
            print(cur.value)
            cur = cur.next
        
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        
        temp = self.tail
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        temp.prev = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True
    
    def pop_first(self):
        if self.head is None:
            return None
        
        temp = self.head
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        temp.next = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index > self.length // 2:
            cur = self.tail
            for _ in range(self.length - index - 1):
                cur = cur.prev
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next

        return cur
    
    def set(self, index, value):
        temp = self.get(index)

        if temp is not None:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        before = self.get(index - 1)
        new_node = Node(value)
        new_node.next = before.next
        new_node.next.prev = new_node
        before.next = new_node
        new_node.prev = before

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        before = self.get(index - 1)
        temp = before.next

        before.next = temp.next
        temp.next.prev = before

        temp.prev = None
        temp.next = None

        self.length -= 1

        return temp


    def reverse(self):
        cur = self.head
        prev = None
        self.tail = self.head

        while cur is not None:
            next_node = cur.next
            cur.next = prev
            cur.prev = next_node

            prev = cur
            cur = next_node

        self.head = prev

l = DoublyLinkedList(0)
l.append(1)
l.append(2)


l.reverse()

l.print_list()