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

# def sum_list(list1, list2):
#     count = 0
#     while(list1 != None and list2!= None):
#         result = list1.data + list2.data
#         carry = result / 10
#         if carry != 0:
#             result = result % 10
#             print result
#             if count > 0:
#                 result += 1
#                 resultant_list.insert(result)
#             else:
#                 print 'iniside else'
#                 resultant_list = LinkedList(Node(result))
#         else:
#             if count > 0:
#                 resultant_list.insert(result)
#             else:
#                 resultant_list = LinkedList(Node(result))
#         list1 = list1.next
#         list2 = list2.next
#         if carry != 0 and count > 0 and list1 != None:
#             list1.data += 1
#         count += 1
#         print result, carry
#     return resultant_list

def sum_list(list1, list2):
    carry = 0
    resultant_list = ''
    value = 0
    while(list1!= None and list2 != None):
        value += carry
        value += list1.data
        value += list2.data
        if (list1.next != None and list2.next != None):
            result = value % 10
        else:
            result = value
        carry = 1 if value >= 10 else 0
        if not resultant_list:
            resultant_list = LinkedList(Node(result))
        else:
            resultant_list.insert(result)
        list1 = list1.next
        list2 = list2.next
        value = 0
    return resultant_list

linkedList1 = LinkedList(Node(6))
linkedList1.insert(1)
linkedList1.insert(7)
linkedList2 = LinkedList(Node(2))
linkedList2.insert(9)
linkedList2.insert(5)
resultant_list = sum_list(linkedList1.head, linkedList2.head).head
result = []
while(resultant_list != None):
    result.append(resultant_list.data)
    resultant_list = resultant_list.next

print result

linkedList1= linkedList1.head
linkedList2= linkedList2.head
while(linkedList1 != None):
    print linkedList1.data
    linkedList1 = linkedList1.next
while(linkedList2 != None):
    print linkedList2.data
    linkedList2 = linkedList2.next
