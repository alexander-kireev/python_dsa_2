class HashTable():
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for index in range(len(self.data_map)):
            print(str(index) + " : " + str(self.data_map[index]))

    
    def set(self, key, value):
        my_hash = self.__hash(key)

        if self.data_map[my_hash] is None:
            self.data_map[my_hash] = []

        self.data_map[my_hash].append([key, value])

    def get(self, key):
        my_hash = self.__hash(key)

        if self.data_map[my_hash] is None:
            return None
        
        for item in self.data_map[my_hash]:
            if item[0] == key:
                return item[1]


    def keys(self):
        keys = []

        for bucket in self.data_map:
            if bucket is not None:
                for item in bucket:
                    keys.append(item[0])

        return keys

