class Stack:
    def __init__(self, arr_size = 0):
        self.arr = [0]* arr_size
        self.max = len(self.arr) - 1
        self.stack = [-1, -1]

    def push(self, stack_num, data):
        if self.stack[0] + 1 == self.stack[1] or self.stack[0] == self.max or self.stack[1] == 0:
            raise Exception('Stack is overflow')
        else:
            if stack_num == 0:
                top = self.stack[0]
                if top == -1:
                    self.arr[0] = data
                    self.stack[0] = 0
                else:
                    self.increment_top(stack_num)
                    self.arr[self.stack[0]] = data
            elif stack_num == 1:
                top = self.stack[1]
                if top == -1:
                    self.arr[self.max] = data
                    self.stack[1] = self.max
                else:
                    top = self.stack[1] - 1
                    self.arr[top] = data
                    self.decrement_top(stack_num)

    def pop(self, stack_num):
        if self.stack[stack_num] == -1:
            raise Exception('Stack is underflow')
        else:
            if stack_num == 0:
                top = self.stack[0]
                item = self.arr[top]
                self.arr[top] = 0
                self.decrement_top(stack_num)
            elif stack_num == 1:
                top = self.stack[1]
                item = self.arr[top]
                self.arr[top] = 0
                if top == self.max:
                    self.stack[stack_num] = -1
                else:
                    self.increment_top(stack_num)
            return item

    def increment_top(self, stack_num):
        self.stack[stack_num] = self.stack[stack_num] + 1

    def decrement_top(self,stack_num):
        self.stack[stack_num] = self.stack[stack_num] - 1

    def display(self):
        print self.arr


s = Stack(6)
s.push(0, 2)
s.push(1, 5)
s.push(0, 3)
s.push(0, 5)
s.push(1, 6)
s.push(1, 7)
s.display()
s.pop(0)
s.display()
s.pop(1)
s.display()
s.pop(0)
s.pop(1)
s.display()
s.pop(0)
s.pop(1)
s.display()