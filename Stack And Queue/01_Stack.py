

# IMPLEMENET STACK USING ARRAY


class Stack:
    def __init__(self):
        self.item = []

    def push(self, val):
        self.item.append(val)

    def pop(self):
        if len(self.item) == 0:
            return 'Cannot Pop, Stack is Empty'
        return self.item.pop()
    
    def top(self):
        if len(self.item) == 0:
            return 'Stack is Empty'
        return self.item[-1]
    
    def size(self):
        return len(self.item)
    
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.top())
print(stack.size())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.top())