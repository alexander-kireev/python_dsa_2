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


    def reverse_between(self, start, end):
        # validate start and end
        if start < 0 or end >= self.length or end < 0:
            return
        
        # check if there is anything to reverse
        if self.head is None or self.head.next is None:
            return
        
        # check length sufficient to reverse
        if start == end:
            return
        
        # create dummy node, place it at the start, connect head to it
        dummy = Node(None)
        dummy.next = self.head
        self.head.prev = dummy

        # get start of list
        cur = self.head

        # find first node to reverse
        for _ in range(start):
            cur = cur.next

        # save reference to first node to be reversed
        first = cur

        # get node before first one
        before = first.prev

        prev = before

        # reverse nodes
        for _ in range(end - start + 1):
            # save reference to next node
            next_node = cur.next

            cur.prev = next_node
            cur.next = prev

            prev = cur
            cur = next_node

        before.next = prev
        self.head = dummy.next

        prev.prev = before
        self.head.prev = None

        # connect whatever is left at end to new end of list
        first.next = cur
        if cur is not None:
            cur.prev = first
        else:
            self.tail = first

        



        

dll = DoublyLinkedList(0)
dll.append(1)
dll.append(2)
dll.append(3)


dll.reverse_between(0, 3)
dll.print_list()