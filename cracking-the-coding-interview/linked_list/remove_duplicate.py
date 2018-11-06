from linked_list import LinkedList

class UniqueLinkedList(LinkedList):
    def remove_duplicate(self):
        nodes = []
        n = self.head
        prev = None
        while n != None:
            if n.data in nodes:
                prev.next = n.next
            else:
                nodes.append(n.data)
                prev = n
            n = n.next


if __name__ == '__main__':
    list = UniqueLinkedList()
    list.add(10)
    list.add(20)
    list.add(30)
    list.add(30)
    list.add(20)
    list.add(10)
    list.display()
    list.remove_duplicate()
    list.display()
