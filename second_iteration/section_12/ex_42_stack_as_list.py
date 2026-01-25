class Stack:
    def __init__(self, value=None):
        self.stack_list = []

        if value is not None:
            self.stack_list.append(value)

        self.height = len(self.stack_list)

        if self.stack_list:
            self.top = self.stack_list[-1]
        else:
            self.top = None

    def push(self, value):
        self.stack_list.append(value)
        self.height += 1

    def pop(self):
        temp = self.stack_list.pop()
        if temp is not None:
            self.height -= 1
        return temp
