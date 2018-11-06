class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        n = self.head
        node = Node(data)
        while n.next != None:
            n = n.next
        n.next = node

    def length(self):
        length = 0
        n = self.head
        while n.next != None:
            length += 1
            n = n.next
        return length

    def remove(self, data):
        n = self.head
        prev = None
        while n.next != None:
            if n.data == data:
                if prev:
                    prev.next = n.next
                else:
                    self.head = n.next
            prev = n
            n = n.next

    def display(self):
        n = self.head.next
        elems = []
        while n != None:
            elems.append(n.data)
            n = n.next
        print elems
        return elems

if __name__ == '__main__':
    list = LinkedList()
    list.add(10)
    list.add(20)
    list.add(30)
    list.display()
    print list.length()

    list.remove(20)
    list.display()