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

    def insertion_sort(self):

        if self.length < 2:
            return
        
        being_placed = self.head.next
        new_head = self.head
        new_head.next = None

        dummy = Node(None)
        dummy.next = new_head

        

        for _ in range(self.length - 1):
            next_node = being_placed.next
            being_placed.next = None
            cur = dummy

            while cur.next is not None:
                if cur.next.value >= being_placed.value:
                    being_placed.next = cur.next
                    cur.next = being_placed
                    break
                elif cur.next.next is None:
                    cur.next.next = being_placed
                    break
                else:
                    cur = cur.next
            
            being_placed = next_node

        self.head = dummy.next

        self.tail = self.head

        while self.tail.next is not None:
            self.tail = self.tail.next
        





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

