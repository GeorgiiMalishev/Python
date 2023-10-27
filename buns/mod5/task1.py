class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.pref
        print()


stack = Stack()
stack.print()
stack.pop()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
value = stack.pop()
stack.print()
