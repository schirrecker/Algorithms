'''
     Data structure: 
    [ (value, link), (value, link), ..., (value, None)]
    to build list, create initial element, then add more element
    functions: add, insert, delete
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def print(self):
        node = self
        while node != None: 
            print (node.data)
            node = node.next

    def insert(self, node):
        pass

    def remove(self):
        pass

    def first_node(self):
        pass

    def last_node(self):
        pass

    def pop(self):  # remove last element
        pass

    def push(self, node):  # replace first element
        pass

node1 = Node ("Alois")
node2 = Node("Stephan")
node3 = Node("Sihem")

node1.next = node2
node2.next = node3

node1.print()


