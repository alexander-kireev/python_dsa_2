class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class RecursiveBinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        cur = self.root
        prev = None

        while cur is not None:
            prev = cur
            
            if value == cur.value:
                return False
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        if value < prev.value:
            prev.left = new_node
        else:
            prev.right = new_node

        return True
    
    def __r_contains(self, value, current_node):
        if current_node is None:
            return False
        
        if current_node.value == value:
            return True
        
        if current_node.value > value:
            return self.__r_contains(value, current_node.left)
        else:
            return self.__r_contains(value, current_node.right)
    
    def r_contains(self, value):
        return self.__r_contains(value, self.root)
    
    def r_insert(self, value):        
        self.root = self.__r_insert(value, self.root)
    
    def __r_insert(self, value, current_node):
        if current_node is None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self.__r_insert(value, current_node.right)

        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
    
    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)

        elif value == current_node.value:

            if current_node.left is None and current_node.right is None:
                return None
            
            if current_node.right is None:
                return current_node.left
            
            if current_node.left is None:
                return current_node.right
            
            smallest_on_right = self.min_value(current_node.right)
            current_node.value = smallest_on_right
            current_node.right = self.__delete_node(current_node.right, smallest_on_right)

        return current_node
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

t = RecursiveBinarySearchTree()
t.insert(50)
t.insert(40)
t.insert(60)
t.insert(30)
t.insert(48)
t.insert(42)
t.insert(41)
t.insert(43)
t.insert(44)
print(t.delete_node(42))