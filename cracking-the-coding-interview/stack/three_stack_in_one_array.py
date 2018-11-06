class FixedStack:
    number_of_stacks = 3
    values = []
    sizes = [0, 0, 0]
    stack_capacity = None
    list_length = 0
    def __init__(self, stack_limit):
        self.stack_capacity = stack_limit
        self.list_length = self.number_of_stacks * stack_limit
        self.values = [None] * self.list_length
    
    def push(self, stack_number, value):
        if self.is_full(stack_number):
            raise Exception('Stack is full')
        self.sizes[stack_number] += 1
        top_index = self.index_of_top(stack_number)
        self.values[top_index] = value

    def pop(self, stack_number):
        if self.is_empty_stack(stack_number):
            raise Exception('Stack is empty')
        top_index = self.index_of_top(stack_number)
        value = self.values[top_index]
        self.values[top_index] = None
        self.sizes[stack_number] -= 1
        return value

    def is_empty_stack(self, stack_number):
        return self.sizes[stack_number] == 0

    def is_full(self, stack_number):
        return self.sizes[stack_number] == self.stack_capacity

    def index_of_top(self, stack_number):
        offset = stack_number * self.stack_capacity
        size = self.sizes[stack_number]
        print size, offset
        return offset + size - 1
stack = FixedStack(15)
print stack.list_length
print stack.index_of_top(0)
stack.push(0, 2)
stack.push(1,4)
stack.push(2, 8)

stack.push(0, 3)
stack.push(1,9)
stack.push(2, 12)
print stack.values
stack.pop(0)
stack.pop(1)
stack.pop(2)
print stack.values