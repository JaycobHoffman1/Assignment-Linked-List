# Task 1 - Implement the **Node** class to represent individual nodes in the doubly linked list.

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Task 2: Implement the SinglyLinkedList class with methods for insertion, deletion, and traversal.

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data, index=None):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif index is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            current = self.head
            count = 0
            while current and count < index:
                count += 1
                current = current.next
            if not current:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                current.prev = new_node

    def delete(self, key=None, index=None):
        if not self.head:
            return
        if index is not None:
            current = self.head
            count = 0
            while current and count < index:
                count += 1
                current = current.next
            if not current:
                return
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == self.head:
                self.head = current.next
            if current == self.tail:
                self.tail = current.prev
        else:
            current = self.head
            while current and current.data != key:
                current = current.next
            if current:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev

    def traversal(self):
        print("Task 3 - Linked list elements:")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Task 3: Test the implemented functionality by performing various operations on the linked list.

my_ll = DoublyLinkedList()
my_ll.append("1")
my_ll.append("2")
my_ll.append("3")
my_ll.delete("2")
my_ll.traversal()