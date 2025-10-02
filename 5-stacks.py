def push(S, item, top, MAX):
    if top==MAX-1:
        print("Overflow")
        return top
    else:
        top+=1
        S.append(item)
        return top
    
def pop(S, top, MAX):
    if top==-1:
        return (-1, -1)
    else:
        temp=S[top]
        top-=1
        del S[-1]
        return (temp, top)
    
def disp(S, top):
    print("Stack")
    for i in range(top+1):
        print(S[i],' ')


class StackOperations:
    def __init__(self):
        self.top = -1
        self.stack = []
        self.max = 5
        
    def push(self, item):
        top = self.top
        stack = self.stack
        max = self.max
        if top == max - 1:
            print('Overflow') 
            return top
        else:
            top += 1
            stack.append(item)
            return top
        
    def pop(self):
        top = self.top
        if top == -1:
            return ('Undeflow')
        else:
            stack = self.stack
            temp = stack[top]
            top -= 1
            del stack[-1]
            return (temp, top)
        
    def display(self):
        print("Stack")
        top = self.top
        stack = self.stack
        for i in range(top + 1):
            print(stack[i], ' ')
            
    def is_overflow(self):
        max = self.max
        top = self.top
        if top == max - 1:
            return True
        else:
            return False
        
    def is_underflow(self):
        top = self.top
        if top == -1:
            return True
        else:
            return False


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []   # using Python list as underlying storage
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.size
    
    def push(self, item):
        if self.isFull():
            print("Stack Overflow! Cannot push", item)
        else:
            self.stack.append(item)
            print(f"Pushed {item} to stack")
    
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! Nothing to pop")
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[-1]
    
    def display(self):
        print("Stack (top -> bottom):", self.stack[::-1])

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
print("Top element:", s.peek())
print("Popped:", s.pop())
s.display()


## Two Stacks using single list ## 

def push1(item, top1, top2, stack):
    if top1 + 1 == top2:
        print("Stack Overflow in Stack 1! Cannot push", item)
        return top1
    else:
        top1 += 1
        stack[top1] = item
        print(f"Pushed {item} to Stack 1")
        return top1
        
def push2(item, top1, top2, stack):
    if top2 - 1 == top1:
        print("Stack Overflow in Stack 2! Cannot push", item)
        return top2
    else:
        top2 -= 1
        stack[top2] = item
        print(f"Pushed {item} to Stack 2")
        return top2
        
def pop1(top1, stack):
    if top1 == -1:
        print("Undeflow in Stack 1! Nothing to pop")
        return top1, None
    item = stack[top1]
    stack[top1] = None
    top1 -= 1
    return top1, item

def pop2(top2, size, stack):
    if top2 == size:
        print("Underflow in Stack 2! Nothing to pop")
        return top2, None
    item = stack[top2]
    stack[top2] = None
    top2 -= 1
    return top2, item

def display(stack):
    print("Stack (top -> bottom):", [x for x in stack if x is not None])

def init():
    MAX=5
    S=MAX*[0]
    top1=-1
    top2=MAX
    return(S, MAX, top1, top2)

S, MAX, top1, top2=init()
while True:
    print("1. Push in Stack 1")
    print("2. Push in Stack 2")
    print("3. Pop from Stack 1")
    print("4. Pop from Stack 2")
    print("5. Display Stacks")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter item to push in Stack 1: "))
        top1 = push1(item, top1, top2, S)
    elif choice == 2:
        item = int(input("Enter item to push in Stack 2: "))
        top2 = push2(item, top1, top2, S)
    elif choice == 3:
        top1, item = pop1(top1, S)
        if item is not None:
            print("Popped from Stack 1:", item)
    elif choice == 4:
        top2, item = pop2(top2, MAX, S)
        if item is not None:
            print("Popped from Stack 2:", item)
    elif choice == 5:
        display(S)
    elif choice == 6:
        break
    else:
        print("Invalid choice! Please try again.")


class TwoStacks:
    def __init__(self, size):
        self.size = size  # maximum size of stack
        self.stack = [None] * size  # single list for two stacks
        self.top1 = -1    # Stack 1 starts from left
        self.top2 = size  # Stack 2 starts from right
    
    def push1(self, item):
        if self.top1 + 1 == self.top2:
            print("Stack Overflow in Stack 1! Cannot push", item)
        else:
            self.top1 += 1
            self.stack[self.top1] = item
            print(f"Pushed {item} to Stack 1")
    
    def push2(self, item):
        if self.top2 - 1 == self.top1:
            print("Stack Overflow in Stack 2! Cannot push", item)
        else:
            self.top2 -= 1
            self.stack[self.top2] = item
            print(f"Pushed {item} to Stack 2")
    
    def pop1(self):
        if self.top1 == -1:
            print("Stack Underflow in Stack 1! Nothing to pop")
            return None
        item = self.stack[self.top1]
        self.stack[self.top1] = None
        self.top1 -= 1
        return item
    
    def pop2(self):
        if self.top2 == self.size:
            print("Stack Underflow in Stack 2! Nothing to pop")
            return None
        item = self.stack[self.top2]
        self.stack[self.top2] = None
        self.top2 += 1
        return item
    
    def display(self):
        print("Stack (top -> bottom):", [x for x in self.stack if x is not None])
        
        
ts = TwoStacks(10)
ts.push1(10)
ts.push2(20)
ts.push1(30)
ts.push2(40)    
ts.display()
print("Popped from Stack 1:", ts.pop1())
print("Popped from Stack 2:", ts.pop2())
ts.display()


class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1              # Stack1 starts from left
        self.top2 = size            # Stack2 starts from right
    
    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow in Stack1!")
    
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow in Stack2!")
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack1 Underflow!")
            return None
    
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack2 Underflow!")
            return None
    
    def display(self):
        print("Stack1:", self.arr[:self.top1+1])
        print("Stack2:", self.arr[self.top2:])
        print("Full Array:", self.arr)
        
        
