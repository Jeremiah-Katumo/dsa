## Simple Queue Implementation ##

def enqueue(Q, front, rear, MAX, item):
    if rear == MAX-1:
        print("Queue Overflow")
        return rear
    elif front == -1 and rear == -1:
        front = 0
        rear = 0
        Q[rear] = item   # Insert item at rear Q.append(item)
        return rear, front
    else:
        rear += 1
        Q[rear] = item   # Insert item at rear Q.append(item)
        return rear, front
        
def dequeue(Q, front, rear):
    if front == -1 and rear == -1:
        print("Queue Overflow")
        return (-1, -1, -1)
    elif front == rear:
        temp = Q[front]
        front = -1
        rear = -1
        return (temp, front, rear)
    else:
        temp = Q[front]
        Q[front] = 0
        front += 1
        return (temp, front, rear)

def enqueue(item, Q, front, rear, MAX):
    if (rear+1)%MAX == front:
        print("Queue Overflow")
        return rear
    else:
        if front == -1:
            front = 0
        rear = (rear + 1) % MAX
        Q.append(item)
        return rear, front
    
def enqueue_priority(item, Q, front, rear, MAX):
    if (rear+1)%MAX == front:
        print("Queue Overflow")
        return rear
    else:
        if front == -1:
            front = 0
            rear = 0
            Q.append(item)
            return rear, front
        else:
            i = rear
            while True:
                if item > Q[i]:
                    if i == front:
                        front = (front - 1 + MAX) % MAX
                        Q.insert(front, item)
                        rear = (rear + 1) % MAX
                        return rear, front
                    else:
                        i = (i - 1 + MAX) % MAX
                else:
                    Q.insert((i + 1) % MAX, item)
                    rear = (rear + 1) % MAX
                    return rear, front
    
def dequeue(Q, front, rear, MAX):
    if front == -1:
        print("Queue Underflow")
        return (-1, -1, -1)
    else:
        item = Q[front]
        if front == rear:
            front = -1
            rear = -1
        else:
            front = (front + 1) % MAX
        del Q[0]
        return (item, front, rear)
    
def display(Q, front, rear, MAX):
    if front == -1:
        print("Queue is empty")
    else:
        i = front
        print("Queue elements are:")
        while True:
            print(Q[i], end=' ')
            if i == rear:
                break
            i = (i + 1) % MAX
        print()
    

## Circular Queue Implementation ##

def circular_enqueue(item, Q, front, rear, MAX):
    if front == -1 and rear == -1:
        front = 0
        rear = 0
        Q[rear] = item   # Insert item at rear Q.append(item)
        return rear, front
    elif (rear + 1) % MAX == front:
        print("Queue Overflow")
        return rear, front
    else:
        rear = (rear + 1) % MAX
        Q[rear] = item   # Insert item at rear Q.append(item)
        return rear, front
    
def circular_dequeue(Q, front, rear, MAX):
    if front == -1 and rear == -1:
        print("Queue Underflow")
        return (-1, -1, -1)
    elif front == rear:
        temp = Q[front]
        front = -1
        rear = -1
        return (temp, front, rear)
    else:
        temp = Q[front]
        Q[front] = 0
        front = (front + 1) % MAX
        return (temp, front, rear)
    

## Priority Queue Implementation ##

def priority_enqueue(item, Q, front, rear, MAX):
    if (rear + 1) % MAX == front:
        print("Queue Overflow")
        return rear, front
    else:
        if front == -1:
            front = 0
            rear = 0
            Q.append(item)
            return rear, front
        else:
            i = rear
            while True:
                if item > Q[i]:
                    if i == front:
                        front = (front - 1 + MAX) % MAX
                        Q.insert(front, item)
                        rear = (rear + 1) % MAX
                        return rear, front
                    else:
                        i = (i - 1 + MAX) % MAX
                else:
                    Q.insert((i + 1) % MAX, item)
                    rear = (rear + 1) % MAX
                    return rear, front
                

## Scheduling using Priority Queue ##

def priority_dequeue(Q, front, rear, MAX):
    if front == -1:
        print("Queue Underflow")
        return (-1, -1, -1)
    else:
        item = Q[front]
        if front == rear:
            front = -1
            rear = -1
        else:
            front = (front + 1) % MAX
        del Q[0]
        return (item, front, rear)
    
## Double Ended Queue Implementation ##

def deque_enqueue_front(item, Q, front, rear, MAX):
    if (rear + 1) % MAX == front:
        print("Queue Overflow")
        return rear, front
    else:
        if front == -1:
            front = 0
            rear = 0
            Q.append(item)
            return rear, front
        else:
            front = (front - 1 + MAX) % MAX
            Q.insert(front, item)
            return rear, front
        
def deque_enqueue_rear(item, Q, front, rear, MAX):
    if (rear + 1) % MAX == front:
        print("Queue Overflow")
        return rear, front
    else:
        if front == -1:
            front = 0
            rear = 0
            Q.append(item)
            return rear, front
        else:
            rear = (rear + 1) % MAX
            Q.append(item)
            return rear, front
        
def deque_dequeue_front(Q, front, rear, MAX):
    if front == -1:
        print("Queue Underflow")
        return (-1, -1, -1)
    else:
        item = Q[front]
        if front == rear:
            front = -1
            rear = -1
        else:
            front = (front + 1) % MAX
        del Q[0]
        return (item, front, rear)
    
def deque_dequeue_rear(Q, front, rear, MAX):
    if front == -1:
        print("Queue Underflow")
        return (-1, -1, -1)
    else:
        item = Q[rear]
        if front == rear:
            front = -1
            rear = -1
        else:
            rear = (rear - 1 + MAX) % MAX
        del Q[-1]
        return (item, front, rear)
    
## Stack and queue using DEQueue ##

def stack_push(item, Q, front, rear, MAX):
    return deque_enqueue_rear(item, Q, front, rear, MAX)
        
def stack_pop(Q, front, rear, MAX):
    return deque_dequeue_rear(Q, front, rear, MAX)
    
def queue_enqueue(item, Q, front, rear, MAX):
    return deque_enqueue_rear(item, Q, front, rear, MAX)

def queue_dequeue(Q, front, rear, MAX):
    return deque_dequeue_front(Q, front, rear, MAX)


## Generating Binary Numbers using Queue ##

from collections import deque

def recursive_binary(n, current=""):
    if len(current) == n:
        print(current)
        return
    recursive_binary(n, current + "0")
    recursive_binary(n, current + "1")
    
print("Binary numbers using recursive approach:")
print(recursive_binary(5))

def stack_binary(n):
    stack = [""]
    count = 0
    while count < n:
        current = stack.pop()
        if len(current) == n:
            print(current)
            count += 1
        else:
            stack.append(current + "1")
            stack.append(current + "0")
            
print("Binary numbers using stack approach:")
print(stack_binary(5))

def queue_binary(n):   # Efficient approach using queue
    Q = deque()   # Initialize a queue
    Q.append("1")
    result = []
    for _ in range(n):
        front = Q.popleft()  # Dequeue operation
        result.append(front)
        Q.append(front + "0")
        Q.append(front + "1")
    return result

print("Binary numbers using queue approach:")
print(queue_binary(5))


## Stack using two queues ##

# 1. Make push operation costly
class StackUsingQueues: 
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Step 1: Push x to q2
        self.q2.append(x)
        # Step 2: Move everything from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Step 3: Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1:
            return self.q1.popleft()
        return None  # Stack underflow

    def top(self):
        if self.q1:
            return self.q1[0]
        return None

    def isEmpty(self):
        return len(self.q1) == 0

s = StackUsingQueues()
s.push(10)
s.push(20)
s.push(30)
print(s.top())   # 30
print(s.pop())   # 30
print(s.top())   # 20
print(s.isEmpty())  # False

# 2. Make pop operation costly
class StackUsingQueuesPopCostly: 
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            return None  # Stack underflow
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped_item = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped_item

    def top(self):
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_item = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return top_item

    def isEmpty(self):
        return len(self.q1) == 0
    
    
## Stack using single queue ##

class StackUsingSingleQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.q:
            return self.q.popleft()
        return None  # Stack underflow

    def top(self):
        if self.q:
            return self.q[0]
        return None

    def isEmpty(self):
        return len(self.q) == 0
    
## Stack using single queue (Alternative Method) ##

class StackUsingSingleQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        size = len(self.q)
        self.q.append(x)
        # Rotate previous elements behind the new one
        for _ in range(size):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return None
        return self.q.popleft()

    def top(self):
        if not self.q:
            return None
        return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0


## Scheduling using Queue ##

def round_robin(processes, burst_time, quantum):
    queue = deque(processes)
    remaining = dict(zip(processes, burst_time))
    time = 0

    while queue:
        p = queue.popleft()
        if remaining[p] > quantum:
            time += quantum
            remaining[p] -= quantum
            queue.append(p)
        else:
            time += remaining[p]
            print(f"{p} finished at time {time}")
            remaining[p] = 0

round_robin(["P1","P2","P3"], [5,3,8], 2)
