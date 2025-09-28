
## ONE-Way Linked Lists ##

class OneWayNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def display_node(self):
        print(self.data, end=' ')
        
class OneWayLinkedList:
    def __init__(self, data1):
        self.first = OneWayNode(data1)
        
    def insert_beg(self, data):
        temp = OneWayNode(data)
        temp.next = self.first
        self.first = temp
        
    def display(self):
        print('List\t:', end=' ')
        ptr = self.first
        while (ptr != None):
            ptr.display_node()
            ptr = ptr.next
            
    def insert_end(self, data):
        temp = OneWayNode(data)
        ptr = self.first
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
        temp.next = None
    
    def insert_after(self, data, data1):
        ptr = self.first
        while (ptr != None):
            if (ptr.data == data1):
                temp = OneWayNode(data)
                temp.next = ptr.next
                ptr.next = temp
                return
            ptr = ptr.next
        print(f'Search Failed. {data1} not in list.')
    # def insert_after(self, data, data1):
    #     flag = 0
    #     temp = OneWayNode(data)
    #     ptr = self.first
    #     while (ptr.next != None):
    #         if (ptr.data == data1):
    #             flag += 1
    #             break
    #         ptr = ptr.next
    #     if (flag == 0):
    #         print('Search Failed')
    #     else:
    #         ptr1 = ptr.next
    #         ptr.next = temp
    #         temp.next = ptr1
            
    def delete_first(self):
        if (self.first != None):
            temp1 = self.first.data
            self.first = self.first.next
            return temp1
        else:
            print('Underflow')
            
    def delete_end(self):
        ptr = self.first
        if (ptr == None):
            print('Underflow')
        elif (ptr.next == None):
            temp1 = ptr.data
            self.first = None
            return temp1
        else:
            while (ptr.next.next != None):
                ptr = ptr.next
            temp1 = ptr.next.data
            ptr.next = None
            return temp1
        
    def delete_after(self, data1):
        ptr = self.first
        while (ptr != None):
            if (ptr.data == data1):
                if (ptr.next == None):
                    print(f'Nothing after: {data1}')
                    return
                temp1 = ptr.next.data
                ptr.next = ptr.next.next
                return temp1
            ptr = ptr.next
        print('Search Failed! {data1} not in list.')
    # def delete_after(self, data1):
    #     if (self.first == None):
    #         print('Underflow')
    #     else:
    #         flag = 0
    #         ptr = self.first
    #         while (ptr != None):
    #             if (ptr.data == data1):
    #                 flag += 1
    #                 break
    #             else:
    #                 ptr = ptr.next
    #         if (flag == 0):
    #             print('Search Failed!')
    #         else:
    #             if (ptr.next == None):
    #                 print(f'Nothing after: {data1}')
    #             else:
    #                 ptr1 = ptr.next
    #                 ptr2 = ptr1.next
    #                 temp1 = ptr1.data
    #                 ptr.next = ptr2
    #                 return temp1

listt = [2,8,7,6,9,5,3,10]
linked_list = OneWayLinkedList(listt)
# for val in listt[1:]:
#     print(f"Inserted at the End: {linked_list.insert_end(val)}")
    
# print(f"1-Way Linked List Insertion Beginning: {linked_list.insert_beg(99)}")
print(f'1-Way Linked List Insertion After: {linked_list.insert_after(55, 7)}')
# print(f'1-Way Linked List Insertion End: {linked_list.insert_end(77)}')
# print(f'1-Way Linked List Deletion Beginning: {linked_list.delete_first()}')
# print(f'1-Way Linked List Deletion End: {linked_list.delete_end()}')
# print(f'1-Way Linked List Deletion After: {linked_list.delete_after(6)}')
print(f"1-Way Linked List Display: {linked_list.display()}")



class OneWayNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def display_node(self):
        print(self.data, end=' ')   

class OneWayLinkedList:
    def __init__(self, data1=None):
        self.first = None
        if data1 is not None:   # allow creating empty list or from first node
            self.first = OneWayNode(data1)
    
    # ✅ Helper method to create linked list from Python list
    def from_list(self, data_list):
        if not data_list:
            print('Linked list is empty!')
            return
        self.first = OneWayNode(data_list[0])
        ptr = self.first
        for val in data_list[1:]:
            ptr.next = OneWayNode(val)
            ptr = ptr.next
    
    def insert_beg(self, data):
        temp = OneWayNode(data)
        temp.next = self.first
        self.first = temp
        
    def display(self):
        print('List\t:', end=' ')
        ptr = self.first
        while ptr:
            ptr.display_node()
            ptr = ptr.next
        print()
        
    def insert_end(self, data):
        temp = OneWayNode(data)
        if not self.first:
            self.first = temp
            return
        ptr = self.first
        while ptr.next:
            ptr = ptr.next
        ptr.next = temp
        
    def insert_after(self, data, data1):
        ptr = self.first
        while ptr:
            if ptr.data == data1:
                temp = OneWayNode(data)
                temp.next = ptr.next
                ptr.next = temp
                return
            ptr = ptr.next
        print('Search Failed')
    
    def delete_first(self):
        if self.first:
            temp1 = self.first.data
            self.first = self.first.next
            return temp1
        print('Underflow')
    
    def delete_end(self):
        if not self.first:
            print('Underflow')
            return
        if not self.first.next:
            temp1 = self.first.data
            self.first = None
            return temp1
        ptr = self.first
        while ptr.next.next:
            ptr = ptr.next
        temp1 = ptr.next.data
        ptr.next = None
        return temp1
    
    def delete_after(self, data1):
        ptr = self.first
        while ptr:
            if ptr.data == data1:
                if not ptr.next:
                    print(f'Nothing after: {data1}')
                    return
                temp1 = ptr.next.data
                ptr.next = ptr.next.next
                return temp1
            ptr = ptr.next
        print('Search Failed!')

listt = [2, 8, 7, 6, 9, 5, 3, 10]
linked_list = OneWayLinkedList()
linked_list.from_list(listt)
# Insert at beginning
linked_list.insert_beg(99)
# Insert at end
linked_list.insert_end(77)
# Insert after 9
linked_list.insert_after(5, 9)
# Display linked list
linked_list.display()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('Linked list is empty!')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)
    
    def insert_end(self, data):
        temp = Node(data, None)
        if self.head is None:
            self.head = temp
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = temp
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, idx):
        if idx < 0 or idx >= self.get_length():
            raise Exception('Invalid Index')
        
        if idx == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def insert_at(self, idx, data):
        if idx < 0 or idx > self.get_length():  # allow inserting at end
            raise Exception('Invalid Index')
        
        if idx == 0:
            self.insert_beg(data)
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    def insert_after_value(self, data, data1):
        itr = self.head
        while itr:
            if itr.data == data1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next     
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "ovacado", "pawpaw", "watermelon"])
    ll.insert_beg(6)
    ll.insert_end(49)
    ll.get_length()
    ll.remove_at(3)
    ll.insert_at(0, 'mango')
    ll.print()

        
## TWO-Way Linked Lists ##

class TwoWayNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def display_node(self):
        print(self.data, end=' ')

class TwoWayLinkedList:
    def __init__(self, data1):
        self.first = data1
        
    def insert_beg(self, data):
        temp = TwoWayNode(data)
        temp.next = self.first
        self.first = temp
        
    def display(self):
        print('List\t:', end=' ')
        ptr = self.first
        while (ptr != None):
            ptr.display_node()
            ptr = ptr.next
            
    def insert_end(self, data):
        temp = TwoWayNode(data)
        ptr = self.first
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
        temp.next = None
        
    def insert_after(self, data, data1):
        flag = 0
        temp = TwoWayNode(data)
        ptr = self.first
        while (ptr.next != None):
            if (ptr.data == data1):
                flag += 1
                break
            ptr = ptr.next
        if (flag == 0):
            print('Search Failed!')
        else:
            ptr1 = ptr.next
            ptr.next = temp
            temp.prev = ptr
            temp.next = ptr1
            ptr1.prev = temp
            
    def delete_first(self):
        if (self.first != None):
            temp1 = self.first.data
            self.first = self.first.next
            return temp1
        else:
            print('Underflow')
            
    def delete_end(self):
        ptr = self.first
        if (ptr == None):
            print('Underflow')
        elif (ptr.next == None):
            temp1 = ptr.data
            self.first = None
            return temp1
        else:
            while (ptr.next.next != None):
                ptr = ptr.next
            temp1 = ptr.next.data
            ptr.next = None
            return temp1
        
    def delete_after(self, data1):
        if (self.first == None):
            print('Undeflow')
        else:
            flag = 0
            ptr = self.first
            while (ptr.next != None):
                if (ptr.data == data1):
                    flag += 1
                    break
                else:
                    ptr = ptr.next
            if (flag == 0):
                print('Search Failed!')
            else:
                if (ptr.next == None):
                    print(f'Nothing after {data1}')
                else:
                    ptr1 = ptr.next
                    ptr2 = ptr1.next
                    temp1 = ptr1.data
                    ptr.next = ptr2
                    return temp1
             
                
# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Display list forward
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " <--> "
            itr = itr.next
        llstr += "None"
        print(llstr)

    def insert_beg(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        node.prev = itr

    def insert_at(self, pos, data):
        if pos < 0:
            raise Exception("Invalid position")

        if pos == 0:
            self.insert_beg(data)
            return

        itr = self.head
        count = 0
        while itr and count < pos - 1:
            itr = itr.next
            count += 1
        if itr is None:
            raise Exception("Position out of range")

        node = Node(data)
        node.next = itr.next
        node.prev = itr
        if itr.next:
            itr.next.prev = node
        itr.next = node

    def delete_beg(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    def delete_at(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos < 0:
            raise Exception("Invalid position")

        if pos == 0:
            self.delete_beg()
            return

        itr = self.head
        count = 0
        while itr and count < pos:
            itr = itr.next
            count += 1
        if itr is None:
            raise Exception("Position out of range")

        if itr.next:
            itr.next.prev = itr.prev
        if itr.prev:
            itr.prev.next = itr.next

dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.display()
dll.insert_beg(5)
dll.display()
dll.insert_at(2, 15)  # Insert 15 at position 2
dll.display()
dll.delete_beg()
dll.display()
dll.delete_end()
dll.display()
dll.delete_at(1)  # Delete element at position 1
dll.display()
             
                
## Cyclic List ##

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def display_node(self):
        print(self.data, end=' ')
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        elements = []
        if self.head is None:
            return elements
        
        itr = self.head     # initialize a pointer
        while True:
            elements.append(itr.data)
            itr = itr.next
            if itr == self.head:
                break
        return elements
    
    def insert_beg(self, data):
        node = CircularNode(data)  # create a new node
        if self.head is None:  # if list is empty:
            self.head = node   # make head = node
            node.next = node   # point node.next to itself
        else:
            itr = self.head
            while itr.next != self.head:  # treverse to the last node
                itr = itr.next
            node.next = self.head
            itr.next = node
            self.head = node
            
    def insert_end(self, data):
        node = CircularNode(data)
        if self.head is None:
            self.head = node
            node.next = node
        else:
            itr = self.head
            while itr.next != self.head:
                itr = itr.next
            itr.next = node         # insert the new node
            node.next = self.head   # point address of new/last node to head
            
    def insert_after(self, key, data):
        if self.head is None:       # if list is empty
            print('Underflow')
            return
        itr = self.head
        while itr:
            if itr.data == key:
                node = CircularNode(data)
                node.next = itr.next      # set node.next to pointer.next
                itr.next = node           # point the pointer.next to the new node
                return
            itr = itr.next
            if itr == self.head:
                print(f"Key {key} not found")
                break
            
    def delete_beg(self):
        if self.head is None:
            print("Underflow")
            return
        if self.head.next == self.head:   # if the list has a single node
            self.head = None
        else:
            itr = self.head
            while itr.next != self.head:  # traverse to the last node in cyclic list
                itr = itr.next
            itr.next = self.head.next
            self.head = self.head.next
            
    def delete_end(self):
        if self.head is None:
            print('Underflow')
            return
        if self.head.next == self.head:
            self.head = None
        else:
            itr = self.head
            prev = None
            while itr.next != self.head:
                prev = itr
                itr = itr.next
            prev.next = self.head
            
    def delete_after(self, key):
        if self.head is None:
            print('Underflow')
            return
        itr = self.head
        while itr:
            if itr.data == key:
                if itr.next == self.head:
                    print("No node exists after the given key")
                    return
                else:
                    itr.next = itr.next.next
                    return
            itr = itr.next
            if itr == self.head:
                print(f"Key {key} not found")
                break
            
cll = CircularLinkedList()

cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_at_end(40)
print("Initial List:", cll.display())
cll.insert_at_begin(5)
print("After Insertion at Beginning:", cll.display())
cll.insert_at_end(50)
print("After Insertion at End:", cll.display())
cll.insert_after(20, 25)
print("After Insertion After 20:", cll.display())
cll.delete_at_begin()
print("After Deletion at Beginning:", cll.display())
cll.delete_at_end()
print("After Deletion at End:", cll.display())
cll.delete_after(25)
print("After Deletion After 25:", cll.display())

## Stacks ##

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def display_node(self):
        print(self.data, end=' ')
        
class StackList:
    def __init__(self, data1):
        self.first = StackNode(data1)
        
    def display(self):
        print('List\\t:', end=' ')
        ptr = self.first
        while (ptr != None):
            ptr.display_node()
            ptr = ptr.next
        print()
            
    def insert_end(self, data):
        temp = StackNode(data)
        ptr = self.first
        while (ptr.next != None):
            ptr = ptr.next 
        ptr.next = ptr
        temp.next = None
    
    def delete_end(self):
        ptr = self.first
        if (ptr == None):
            print('Underflow')
        elif (ptr.next == None):
            temp1 = ptr.data
            self.first =None
            return temp1
        else:
            while (ptr.next.next != None):
                ptr = ptr.next
            temp1 = ptr.next.data
            ptr.next = None
            return temp1
        

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    # a. PUSH
    def push(self, data):
        if len(self.stack) == self.capacity:
            print("Stack Overflow!")
            return
        self.stack.append(data)
        print(f"Pushed: {data}")
    
    # b. POP
    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return None
        return self.stack.pop()
    
    # c. PEEK
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]
    
    # d. isEmpty
    def is_empty(self):
        return len(self.stack) == 0
    
    # e. isFull
    def is_full(self):
        return len(self.stack) == self.capacity
    
    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (top -> bottom):", self.stack[::-1])

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top element:", s.peek())
print("Popped:", s.pop())
s.display()
s.push(40)
s.push(50)
s.push(60)
s.push(70)  # Will show overflow
s.display()
         

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def display_node(self):
        print(self.data, end=' ')
        
class QueueList:
    def __init__(self, data1):
        self.first = QueueNode(data1)
        
    def display(self):
        print('List\\t:' , end=' ')
        ptr = self.first
        while (ptr != None):
            ptr.display_node()
            ptr = ptr.next
        print()
    
    def insert_end(self, data):
        temp = QueueNode(data)
        ptr = self.first
        while (ptr.next != None):
            ptr = ptr.next
        temp.next = None
        
    def delete_beg(self):
        if (self.first != None):
            temp1 = self.first.data
            self.first = self.first.next
            return temp1
        else:
            print('Underflow')

    def reverse_list(list1):
        if ((list1.first == None) or (list1.first.next == None)):
            return list1
        else:
            ptr = list1.first
            ptr1 = list1.first.next
            ptr2 = ptr1.next
            # print(ptr.data, ptr1.data, ptr2.data)
            ptr1.next = ptr
            ptr.next = None
            while (ptr2 != None):
                ptr = ptr1
                ptr1 = ptr2
                ptr2 = ptr2.next
                ptr1.next = ptr
            list1.first = ptr1
            return list1
        
    def concatenate_list(self, list1, list2):
        temp1 = StackNode(list1)
        temp2 = StackNode(list2)
        ptr = temp1.first
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp2.first
        
    def check_cycle(self, list1):
        links = set()
        temp = StackNode(list1)
        ptr = self.first
        while (True):
            if (ptr.next == None):
                print('No Cycle')
                break
            if ptr.next not in links:
                links.add(ptr.next)
                ptr = ptr.next
            else:
                print('Cycle')
                break
            

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    # a. ENQUEUE
    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow!")
            return
        self.queue.append(data)
        print(f"Enqueued: {data}")
    
    # b. DEQUEUE
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return None
        return self.queue.pop(0)
    
    # c. PEEK (Front element)
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]
    
    # d. isEmpty
    def is_empty(self):
        return len(self.queue) == 0
    
    # e. isFull
    def is_full(self):
        return len(self.queue) == self.capacity
    
    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (front -> rear):", self.queue)

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Front element:", q.peek())
print("Dequeued:", q.dequeue())
q.display()
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)  # Overflow
q.display()
