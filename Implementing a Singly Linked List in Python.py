# Task 1: Implement the Node class to represent individual nodes in the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Task 2: Implement the SinglyLinkedList class with methods for insertion, deletion, and traversal.

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = prev
                return True
            prev = current
            current = current.next
        return False

    def traversal(self):
        print(" Task 3 - Linked list elements:")
        for data in self:
            print(data, end=" -> ")
        print("None")

# Task 3 - Test the implemented functionality by performing various operations on the linked list.

my_ll = SinglyLinkedList()
my_ll.append("1")
my_ll.append("2")
my_ll.append("3")
my_ll.delete("2")
my_ll.traversal()