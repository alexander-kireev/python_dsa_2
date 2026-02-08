class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        if self.length == 0 and other_list.length == 0:
            return
        
        # set new self.length 
        self.length += other_list.length

        # set dummy node to keep track of future self.head
        dummy = Node(0)
        dummy.next = self.head
        
        # start looping from dummy
        cur = dummy

        # while the other list is not empty
        while other_list.length > 0:

            # if we have reached end of current list, connect tail of current list
            # (which is cur.next) to head of other list, break out of loop
            if cur.next is None:
                cur.next = other_list.head
                other_list.length = 0
                other_list.head = None
                other_list.tail = None
                break
            
            # if the head of other list is smaller than the next value in current list,
            # insert the head of other list BEFORE the next value in current list,
            # removing head of other list, decrementing length of other list
            if other_list.head.value < cur.next.value:
                new_other_list_head = other_list.head.next
                other_list.head.next = cur.next
                cur.next = other_list.head

                cur = cur.next

                other_list.head = new_other_list_head
                other_list.length -= 1
            
            # if head of other list is larger than the next value in current list,
            # move cur pointer ahead
            else:
                cur = cur.next

        # reset self.head, self.tail and self.length
        self.head = dummy.next
        self.tail = self.head

        # get updated self.tail
        while self.tail.next is not None:
            self.tail = self.tail.next

    
l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""