class Node:
    """Node class for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    """Node class for doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    """Singly Linked List implementation"""
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_beginning(self, data):
        """Insert node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data):
        """Insert node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert node at specific position (0-indexed)"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of range")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        if position == self.size:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def insert_after_value(self, data, target_value):
        """Insert node after a specific value"""
        if not self.head:
            raise ValueError("List is empty")
        
        current = self.head
        while current and current.data != target_value:
            current = current.next
        
        if not current:
            raise ValueError(f"Value {target_value} not found")
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at_beginning(self):
        """Delete node at the beginning"""
        if not self.head:
            raise ValueError("List is empty")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def delete_at_end(self):
        """Delete node at the end"""
        if not self.head:
            raise ValueError("List is empty")
        
        if not self.head.next:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        data = current.next.data
        current.next = None
        self.size -= 1
        return data
    
    def delete_at_position(self, position):
        """Delete node at specific position (0-indexed)"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
        
        if position == 0:
            return self.delete_at_beginning()
        
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return data
    
    def delete_by_value(self, value):
        """Delete first occurrence of a value"""
        if not self.head:
            raise ValueError("List is empty")
        
        if self.head.data == value:
            return self.delete_at_beginning()
        
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if not current.next:
            raise ValueError(f"Value {value} not found")
        
        data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return data
    
    def display(self):
        """Display the linked list"""
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

class DoublyLinkedList:
    """Doubly Linked List implementation"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at_beginning(self, data):
        """Insert node at the beginning"""
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def insert_at_end(self, data):
        """Insert node at the end"""
        new_node = DoublyNode(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert_at_position(self, data, position):
        """Insert node at specific position (0-indexed)"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of range")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        if position == self.size:
            self.insert_at_end(data)
            return
        
        new_node = DoublyNode(data)
        current = self.head
        for i in range(position):
            current = current.next
        
        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        self.size += 1
    
    def insert_after_value(self, data, target_value):
        """Insert node after a specific value"""
        if not self.head:
            raise ValueError("List is empty")
        
        current = self.head
        while current and current.data != target_value:
            current = current.next
        
        if not current:
            raise ValueError(f"Value {target_value} not found")
        
        new_node = DoublyNode(data)
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node
        
        current.next = new_node
        self.size += 1
    
    def delete_at_beginning(self):
        """Delete node at the beginning"""
        if not self.head:
            raise ValueError("List is empty")
        
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data
    
    def delete_at_end(self):
        """Delete node at the end"""
        if not self.tail:
            raise ValueError("List is empty")
        
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data
    
    def delete_at_position(self, position):
        """Delete node at specific position (0-indexed)"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
        
        if position == 0:
            return self.delete_at_beginning()
        
        if position == self.size - 1:
            return self.delete_at_end()
        
        current = self.head
        for i in range(position):
            current = current.next
        
        data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return data
    
    def delete_by_value(self, value):
        """Delete first occurrence of a value"""
        if not self.head:
            raise ValueError("List is empty")
        
        current = self.head
        while current and current.data != value:
            current = current.next
        
        if not current:
            raise ValueError(f"Value {value} not found")
        
        data = current.data
        if current == self.head:
            return self.delete_at_beginning()
        elif current == self.tail:
            return self.delete_at_end()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
        return data
    
    def display_forward(self):
        """Display the doubly linked list forward"""
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements))
    
    def display_backward(self):
        """Display the doubly linked list backward"""
        if not self.tail:
            print("List is empty")
            return
        
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements))

class Stack:
    """Stack implementation using linked list"""
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        """Push element onto stack (insert at beginning)"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        """Pop element from stack (delete from beginning)"""
        if not self.top:
            raise ValueError("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def peek(self):
        """Peek at top element without removing"""
        if not self.top:
            raise ValueError("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None
    
    def display(self):
        """Display stack from top to bottom"""
        if not self.top:
            print("Stack is empty")
            return
        
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Top -> " + " -> ".join(elements) + " <- Bottom")

class Queue:
    """Queue implementation using linked list"""
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue(self, data):
        """Enqueue element (insert at rear/end)"""
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        """Dequeue element (delete from front/beginning)"""
        if not self.front:
            raise ValueError("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return data
    
    def front_element(self):
        """Get front element without removing"""
        if not self.front:
            raise ValueError("Queue is empty")
        return self.front.data
    
    def rear_element(self):
        """Get rear element without removing"""
        if not self.rear:
            raise ValueError("Queue is empty")
        return self.rear.data
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front is None
    
    def display(self):
        """Display queue from front to rear"""
        if not self.front:
            print("Queue is empty")
            return
        
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Front -> " + " -> ".join(elements) + " <- Rear")

# Demonstration and testing
if __name__ == "__main__":
    print("=== SINGLY LINKED LIST DEMO ===")
    sll = SinglyLinkedList()
    
    # Insertions
    sll.insert_at_beginning(10)
    sll.insert_at_end(30)
    sll.insert_at_position(20, 1)
    sll.insert_after_value(25, 20)
    print("After insertions:")
    sll.display()
    
    # Deletions
    print(f"\nDeleted from beginning: {sll.delete_at_beginning()}")
    print(f"Deleted from end: {sll.delete_at_end()}")
    print(f"Deleted at position 0: {sll.delete_at_position(0)}")
    sll.display()
    
    print("\n=== DOUBLY LINKED LIST DEMO ===")
    dll = DoublyLinkedList()
    
    # Insertions
    dll.insert_at_beginning(10)
    dll.insert_at_end(30)
    dll.insert_at_position(20, 1)
    dll.insert_after_value(25, 20)
    print("After insertions (forward):")
    dll.display_forward()
    print("After insertions (backward):")
    dll.display_backward()
    
    # Deletions
    print(f"\nDeleted from beginning: {dll.delete_at_beginning()}")
    print(f"Deleted from end: {dll.delete_at_end()}")
    dll.display_forward()
    
    print("\n=== STACK DEMO ===")
    stack = Stack()
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("After pushes:")
    stack.display()
    
    # Pop elements
    print(f"Popped: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    stack.display()
    
    print("\n=== QUEUE DEMO ===")
    queue = Queue()
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("After enqueues:")
    queue.display()
    
    # Dequeue elements
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Front element: {queue.front_element()}")
    print(f"Rear element: {queue.rear_element()}")
    queue.display()