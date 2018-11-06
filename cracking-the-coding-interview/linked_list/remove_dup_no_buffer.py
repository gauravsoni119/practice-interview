from linked_list import LinkedList

class UniqueLinkedList(LinkedList):
    def remove_duplicate(self):
        n = self.head
        while n != None:
            curr_node = n
            while curr_node.next != None:
                if (n.data == curr_node.next.data):
                    curr_node.next = curr_node.next.next
                else:
                    curr_node = curr_node.next
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
