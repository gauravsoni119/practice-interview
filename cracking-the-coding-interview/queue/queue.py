class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add(self, data):
        queue_node = Node(data)
        if self.rear != None:
            self.rear.next = queue_node
        self.rear = queue_node
        if self.front == None:
            self.front = self.rear

    def remove(self):
        if self.front != None:
            self.front = self.front.next
        else:
            raise 'Queue is empty'

    def peek(self):
        return self.front.data

    def is_empty(self):
        return True if self.front == None else False

    def display(self):
        arr = []
        n = self.front
        while n != None:
            arr.append(n.data)
            n = n.next
        return arr

queue = Queue()
print queue.is_empty()
queue.add(10)
queue.add(20)
queue.add(30)
queue.add(40)
print queue.display()
print queue.is_empty()
print queue.peek()
queue.remove()
print queue.display()
print queue.peek()
queue.remove()
queue.remove()
queue.remove()
print queue.display()
print queue.is_empty()