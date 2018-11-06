class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

class LinkedList():
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n
def clone_list(list1):
    list2 = ''
    while(list1 != None):
        if not list2:
            print list1.data
            list2 = LinkedList(Node(list1.data))
        else:
            list2.insert(list1.data)
        list1 = list1.next
    return list2

def is_palindrome(l1, l2):
    while l1 != None and l2 != None:
        if (l1.data != l2.data):
            return False
        l1 = l1.next
        l2 = l2.next
    return True

def is_palindrome_by_iterate_method(linkedList):
    fast = linkedList
    slow = linkedList
    list = []
    while(fast != None and fast.next != None):
        list.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast != None:
        slow = slow.next

    while slow != None:
        elem = list.pop()
        if elem != slow.data:
            return False
        slow = slow.next
    return True

linkedList1 = LinkedList(Node(1))
linkedList1.insert(3)
linkedList1.insert(3)
linkedList1.insert(2)
linkedList2 = clone_list(linkedList1.head)
print is_palindrome(linkedList1.head, linkedList2.head)
linkedList1 = linkedList1.head
linkedList2 = linkedList2.head
while(linkedList1 != None):
    print linkedList1.data
    linkedList1 = linkedList1.next
while(linkedList2 != None):
    print linkedList2.data
    linkedList2 = linkedList2.next

linkedList3 = LinkedList(Node(1))
linkedList3.insert(3)
linkedList3.insert(5)
linkedList3.insert(3)
linkedList3.insert(1)
print is_palindrome_by_iterate_method(linkedList3.head)