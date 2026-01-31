class MaxHeap:
    def __init__(self):
        self.nodes_list = [None]
        
    def _left_child(self, index):
        return index * 2

    
    def _right_child(self, index):
        return index * 2 + 1

        
    def _parent(self, index):
        return index // 2
    
    def _swap(self, index1, index2):
        temp = self.nodes_list[index1]
        self.nodes_list[index1] = self.nodes_list[index2]
        self.nodes_list[index2] = temp

    def insert(self, value):
        in_place = False
        self.nodes_list.append(value)
        index_inserted = len(self.nodes_list) - 1
        
        while not in_place:
            parent_index = self._parent(index_inserted)
            parent_value = self.nodes_list[parent_index]

            if parent_value is None or parent_value >= value:
                in_place = True
            else:
                self._swap(parent_index, index_inserted)
                index_inserted = parent_index
    
    def remove(self):
        if len(self.nodes_list) == 1:
            return False
        
        if len(self.nodes_list) == 2:
            self.nodes_list.pop()
            return True
        
        old_top = self.nodes_list[1]
        self.nodes_list[1] = self.nodes_list.pop()
        self.sink_down(1)

        return old_top


    def sink_down(self, index):
        while True:
            max_index = index

            right_index = self._right_child(index)
            left_index = self._left_child(index)

            if ((left_index <= len(self.nodes_list) - 1) and 
                    (self.nodes_list[left_index] > self.nodes_list[max_index])):
                max_index = left_index
            
            if ((right_index <= len(self.nodes_list) - 1) and
                    (self.nodes_list[right_index] > self.nodes_list[max_index])):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return



            
            


        

    def print_heap(self):
        print(self.nodes_list)

h = MaxHeap()
h.insert(50)
h.insert(60)
h.insert(52)
h.insert(53)

h.remove()
h.print_heap()
