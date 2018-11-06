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


def kth_to_last(head, elem):
    if (head == None):
        return 0
    index = kth_to_last(head.next, elem) + 1
    # print index, elem
    if index == elem:
        print str(elem) + "th to last node is " + str(head.data)
    return index

def kth_to_last_updated(head, k):
    node1 = head
    node2 = head
    for i in range(k):
        if node1 == None:
            return None
        node1 = node1.next
    while(node1 != None):
        node1 = node1.next
        node2 = node2.next
    return node2
linkedList = LinkedList(Node(30))
linkedList.insert(10)
linkedList.insert(20)
linkedList.insert(40)
# linkedList.insert(40)
# linkedList.insert(10)
print linkedList.head.data
print linkedList.head.next.data
print linkedList.head.next.next.data
print linkedList.head.next.next.next.data
print "====================="
# kth_to_last(linkedList.head, 2)
nodes = kth_to_last_updated(linkedList.head, 2)
print nodes.data, ' ', nodes.next.data
nodes1 = kth_to_last_updated(linkedList.head, 1)
print nodes1.data
nodes2 = kth_to_last_updated(linkedList.head, 3)
print nodes2.data, ' ', nodes2.next.data, ' ', nodes2.next.next.data