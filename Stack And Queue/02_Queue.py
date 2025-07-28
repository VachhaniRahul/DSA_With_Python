


class Queue:
    def __init__(self):
        self.item = []

    
    def endqueue(self, val):
        self.item.append(val)

    def dequeue(self):
        if len(self.item) == 0:
            return 'Cannot dequeue, Queue is Empty'
        return self.item.pop(0)
    
    def front(self):
        if len(self.item) == 0:
            return 'Queue is Empty'
        return self.item[0]
    
    def rear(self):
        if len(self.item) == 0:
            return 'Queue not have rear, Queue is Empty'
        return self.item[-1]
    
    def size(self):
        return len(self.item)
    

queue = Queue()
queue.endqueue(10)
queue.endqueue(20)
print(queue.size())
print(queue.front())
print(queue.rear())
queue.endqueue(30)
print(queue.rear())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.rear())