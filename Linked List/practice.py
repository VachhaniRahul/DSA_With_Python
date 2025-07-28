class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        n = Node(val)
        if self.head is None:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n

    def traverse(self):
        if self.head is None:
            print('Linked list is empty')
            return
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    def insert(self, pos, val):
        n = Node(val)
        if self.head is None:
            self.head = n
            return
        if pos == 0:
            n.next = self.head
            self.head = n 
        else:
            count = 0
            cur = self.head
            prev = None

            while count < pos and cur:
                prev = cur
                cur = cur.next
                count += 1
            prev.next = n
            n.next = cur

    def delete(self, val):
        cur = self.head
        if cur is None:
            print('Linked list is empty')
            return
        
        if cur.val == val:
            if cur.next is None:
                self.head = None
            else:
                self.head = cur.next
        else:
            found = False
            prev = None
            while cur:
                if cur.val == val:
                    found = True
                    break
                prev = cur
                cur = cur.next
            if found:
                prev.next = cur.next
            else:
                print('Node Not Found')

    def middle(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        fast = self.head
        slow = self.head
                
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)

    
    def reverse(self):
        cur = self.head
        prev = None
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        self.head = prev

    def cycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                print(slow.val, end=' ')
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                print(count)
                break
        else:
            print('No Cycle Exists')     

    
    def odd_even(self):
        odd = self.head
        if odd is None:
            print('Linked list is empty')
            return
        even = self.head.next
        e_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        
        odd.next = e_head
        self.traverse()

    
    def remove(self, index):
        slow = self.head

        if slow is None:
            print('Linked list is empty')
            return
        
        fast = slow
        
        count = 0

        while count < index and fast and fast.next:
            fast = fast.next
            count += 1
        
        if count < index-1:
            print('Linked list have less node then provided index')
            return
        
        start = True
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            start = False

        if start:
            self.head = self.head.next
        else:
            slow.next = slow.next.next
        self.traverse()





s1 = SinglyLinkedList()
s1.append(10)
s1.append(20)
s1.append(30)
s1.append(40)
s1.append(50)
s1.traverse()
# s1.odd_even()
s1.remove(2)