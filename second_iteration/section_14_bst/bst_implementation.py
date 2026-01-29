class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        cur = self.root
        prev = None

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            
        else:
            while cur is not None:
                prev = cur
                if value < cur.value:
                    cur = cur.left
                elif value > cur.value:
                    cur = cur.right
                elif value == cur.value:
                    return True
            
            if value < prev.value:
                prev.left = new_node
            else:
                prev.right = new_node
            
        return True
        

    def contains(self, value):
        cur = self.root

        while cur is not None:
            if value == cur.value:
                return True
            
            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        
        return False
    

    def get(self, value):
        cur = self.root

        while cur is not None:
            if value == cur.value:
                return cur
            
            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        
        return None

    def get_parent(self, value):
        parent = self.root
        cur = self.root

        while cur is not None:
            if cur.value == value:
                return parent
            
            parent = cur

            if value < cur.value:
                cur = cur.left
            elif value > cur.value:
                cur = cur.right
        
        return None

    def remove(self, value):
        parent = self.get_parent(value)

        # if node exists 
        if parent is not None:
            
            if parent.left is not None and parent.left.value == value:
                node_to_be_deleted = parent.left

                if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
                    parent.left = None
                elif node_to_be_deleted.left is not None and node_to_be_deleted.right is not None:
                    
                    # get smallest
                    smallest = self.get_smallest(node_to_be_deleted.right)

                    smallest_value = smallest.value

                    self.remove(smallest_value)

                    node_to_be_deleted.value = smallest_value

                elif node_to_be_deleted.left is not None:
                    parent.left = node_to_be_deleted.left
                elif node_to_be_deleted.right is not None:
                    parent.left = node_to_be_deleted.right

            elif parent.right is not None and parent.right.value == value:
                node_to_be_deleted = parent.right

                if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
                    parent.right = None
                elif node_to_be_deleted.left is not None and node_to_be_deleted.right is not None:
                    
                    # get smallest
                    smallest = self.get_smallest(node_to_be_deleted.right)

                    smallest_value = smallest.value

                    self.remove(smallest_value)

                    node_to_be_deleted.value = smallest_value

                elif node_to_be_deleted.left is not None:
                    parent.right = node_to_be_deleted.left
                elif node_to_be_deleted.right is not None:
                    parent.right = node_to_be_deleted.right
            
            else:
                node_to_be_deleted = self.root

                if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
                    self.root = None
                elif node_to_be_deleted.left is not None and node_to_be_deleted.right is not None:
                    
                    # get smallest
                    smallest = self.get_smallest(node_to_be_deleted.right)

                    smallest_value = smallest.value

                    self.remove(smallest_value)

                    node_to_be_deleted.value = smallest_value

                elif node_to_be_deleted.left is not None:
                    self.root = node_to_be_deleted.left
                elif node_to_be_deleted.right is not None:
                    self.root = node_to_be_deleted.right
            
            

            return True
        else:
            return False


            
    def get_smallest(self, node):
        cur = node

        while cur.left is not None:
            cur = cur.left

        return cur

t = BinarySearchTree()
t.insert(5)
# t.insert(2)
# t.insert(8)
# t.insert(7)
# t.insert(1)

print(t.root.value)

t.remove(5)

print(t.root)