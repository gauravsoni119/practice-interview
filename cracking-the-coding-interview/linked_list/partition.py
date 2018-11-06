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

    def remove_duplicate(self):
        current_node = self.head
        previous = None
        nodes = []
        while current_node:
            if current_node.data in nodes:
                previous.next = current_node.next
            else:
                previous = current_node
                nodes.append(current_node.data)
            current_node = current_node.next

def partion_linked_list(head, elem):
    before_partion_elem_list = ''
    after_partion_elem_list = ''
    node = head
    while(node != None):
        if node.data < elem:
            if not before_partion_elem_list:
                before_partion_elem_list = LinkedList(Node(node.data))
            else:
                before_partion_elem_list.insert(node.data)
        else:
            if not after_partion_elem_list:
                after_partion_elem_list = LinkedList(Node(node.data))
            else:
                before_partion_elem_list.insert(node.data)
        node = node.next
    # print after_partion_elem_list.head.data, after_partion_elem_list.head.next.data, before_partion_elem_list.next
    # before_partion_elem_list.next = after_partion_elem_list
    head = after_partion_elem_list.head
    while head != None:
        before_partion_elem_list.insert(head.data)
        head = head.next
    return before_partion_elem_list

linkedList = LinkedList(Node(30))
linkedList.insert(60)
linkedList.insert(40)
linkedList.insert(10)
linkedList.insert(20)
linkedList.insert(50)
link_lis = linkedList.head
link_list_data_arr = []
link_list_data_arr_sorted = []
while(link_lis != None):
    link_list_data_arr.append(link_lis.data)
    link_lis = link_lis.next
link_lis = partion_linked_list(linkedList.head, 40).head
while(link_lis != None):
    link_list_data_arr_sorted.append(link_lis.data)
    link_lis = link_lis.next
print link_list_data_arr
print link_list_data_arr_sorted
