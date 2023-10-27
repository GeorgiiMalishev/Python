class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None

        val = self.start.data
        self.start = self.start.nref

        if self.start is None:
            self.end = None

        return val

    def push(self, val):
        new_node = Node(val)

        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def insert(self, n, val):
        n -= 1
        if n < 0:
            return
        elif n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            for i in range(n):
                if current is None:
                    return
                current = current.nref
            if current is None:
                self.push(val)
                return
            new_node = Node(val)
            new_node.nref = current
            new_node.pref = current.pref
            current.pref.nref = new_node
            current.pref = new_node

    def print(self):
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.nref
        print()


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.print()
queue.insert(1, 4)
queue.print()
value = queue.pop()
print(value)
queue.print()
