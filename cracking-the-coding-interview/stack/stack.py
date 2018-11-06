class StackNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = StackNode()

    def push(self, data):
        stack_node = StackNode(data)
        stack_node.next = self.top
        self.top = stack_node

    def pop(self):
        if not self.has_top():
            raise 'Stack is empty'
        item = self.top.data
        self.top = self.top.next
        return item

    def has_top(self): 
        return True if self.top != None else False

    def peek(self):
        print self.top
        if not self.has_top():
            raise 'Stack is empty'
        return self.top.data

    def is_empty(self):
        return not self.has_top()
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print 'Peek item in stack is %d'%stack.peek()
print stack.pop()
print 'Peek item in stack after removing item %d'%stack.peek()
print stack.pop()
print stack.peek()
print stack.is_empty()