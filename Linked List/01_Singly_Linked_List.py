

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()

    def insert(self, index, val):
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            current = self.head
            previous = None

            while count != index and current is not None:
                previous = current
                current = current.next
                count += 1

            previous.next = new_node
            new_node.next = current

    def delete(self, val):
        current = self.head
        previous = None

        if current.val == val:
            if current.next is None:
                self.head = None
            else:
                self.head = current.next
        else:
            found = False
            while current is not None:
                if current.val == val:
                    found = True
                    break
                previous = current
                current = current.next
            if found:
                previous.next = current.next
            else:
                print('Node not found')
             



sll = SinglyLinkList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()
sll.insert(1,15)
sll.traverse()
sll.delete(10)
sll.traverse()
sll.append(40)
sll.traverse()
