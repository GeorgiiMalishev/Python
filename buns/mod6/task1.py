class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get(self, index):
        self._check_index(index)
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def remove(self, index):
        self._check_index(index)
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def insert(self, n, val):
        self._check_index(n)
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(n - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def _check_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

