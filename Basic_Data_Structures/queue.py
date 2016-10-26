class Queue(object):
    
    def __init__(self):
        self.items = list()

    def enqueue(self, item):
        self.items.append(0, item)

    def dequeue(self):
        return self.items.pop()

    def isempty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)
