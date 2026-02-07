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

    def bubble_sort(self):
        dummy = Node(None)
        dummy.next = self.head

        for i in range(self.length - 1):

            prev = dummy
            cur = dummy.next
            switched = False

            for _ in range(i, self.length - 1):

                if cur is not None:
                    next_node = cur.next

                    if next_node is not None:

                        if cur.value > next_node.value:
                            prev.next = next_node
                            cur.next = next_node.next
                            next_node.next = cur
                            prev = next_node
                            switched = True
                        else:
                            prev = cur
                            cur = cur.next

            if not switched:
                
                self.head = dummy.next
                self.tail = self.head

                while self.tail.next is not None:
                    self.tail = self.tail.next
                
                return 
        



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()

print(my_linked_list.tail.value)


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

