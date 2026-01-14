class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        cur = self.head
        pre = self.head

        while cur.next is not None:
            pre = cur
            cur = cur.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return cur
        
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        return True
        
    def pop_first(self):
        if self.length == 0:
            return None
        
        node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        node.next = None
        self.length -= 1
        return node
    
    def get(self, index):
        if self.length <= index or self.length == 0 or index < 0:
            return None
        
        cur = self.head
        position = 0

        while position < index:
            cur = cur.next
            position += 1
        
        return cur

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)  
        else:
            prev_node = self.get(index - 1)
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1
        
        return True

    def set(self, index, value):     
        current_node = self.get(index)
        if current_node is not None:
            current_node.value = value
            return True
        
        return False
    

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev_node = self.get(index - 1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next
            removed_node.next = None
            self.length -= 1
            return removed_node

    def reverse(self):
        if self.length < 2:
            return True
        
        prev = None
        cur = self.head
        self.tail = self.head

        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        self.head = prev
        return True


l = LinkedList(0)
l.append(1)
l.append(2)
l.append(3)

print(l.get(-1))
