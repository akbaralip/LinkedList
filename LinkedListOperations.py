

class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_first(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.ref = self.head
            self.head = node
            return
    def add_between(self, data, after):
        node = Node(data)
        if self.head is None:
            print('There is no node!')
            return
        else:
            current = self.head
            while current:
                if current.value == after:
                    node.ref = current.ref
                    current.ref = node
                    return
                current = current.ref
    def add_to_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.ref:
                current = current.ref
            current.ref = node
            return
    def display(self):
        current = self.head
        while current:
            print(current.value)
            current = current.ref

obj = LinkedList()
# obj.add_to_first(10)
# obj.add_to_first(20)
# obj.add_to_first(40)
# obj.add_between(15,20)

obj.add_to_last(10)
obj.add_to_last(20)

obj.display()