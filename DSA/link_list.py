# class Node(object):
#     def __init__(self,data):
#         self.data = data
#         self.next_node = None

# class LinkedList(object):

#     def __init__(self,node):
#         self.head = node

#     def traverse(self):
#         while self.head is not None:
#             print(self.head.data)
#             self.head = self.head.next_node

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# link_lst = LinkedList(n1)
# n1.next_node = n2
# n2.next_node = n3

# link_lst.traverse()

# print(link_lst.head.data)
# print(link_lst.head.next_node.data)



# ============================ Doubly Link List =======================
'''
    This is my own trick so don't confuse.....
'''

class Node(object):
    def __init__(self,data):
        self.data = data
        self.prev_node = None
        self.next_node = None

class DoublyLinkedList(object):

    def __init__(self,node):
        self.head = node

    def traverse(self):
        current = self.head
        while self.head is not None:
            print("Current ->",self.head.data)
            if self.head.prev_node:
                print("Previous ->",self.head.prev_node.data)
            else:
                print("Previous ->",self.head.prev_node)
            if self.head.next_node:
                print("Next ->",self.head.next_node.data)
            else:
                print("Next ->",self.head.next_node)

            self.head = self.head.next_node
            if self.head:
                self.head.prev_node = current

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

link_lst = DoublyLinkedList(n1)
n1.next_node = n2
n2.next_node = n3

link_lst.traverse()