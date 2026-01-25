class Stack:
    def __init__(self, value=None):
        self.stack_list = []

        if value is not None:
            self.stack_list.append(value)

        self.height = len(self.stack_list)

        self.top = [0]

    def push(self, value):
        self.stack_list.append(value)
        self.height += 1

    def pop(self):
        if self.top is not None:
            self.height -= 1
            return self.stack_list.pop()
        return None
    
    def is_empty(self):
        return self.height == 0
    

def reverse_string(word):
    stack = Stack()
    reversed_string = ""

    for char in word:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string


word = "hello"

print(reverse_string(word))