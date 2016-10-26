class Queue(object):
    
    def __init__(self):
        self.items = list()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isempty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

q = Queue()

q.enqueue(4)
q.enqueue('Dog')
q.size()
print(q.size())
print(q.show())

