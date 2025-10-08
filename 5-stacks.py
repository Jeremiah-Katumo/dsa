## SImp;e Stack Implimentation ##

def push(S, item, top, MAX):
    if top == MAX-1:
        print("Overflow")
        return top
    else:
        top += 1
        S.append(item)
        return top
    
def pop(S, top):
    if top == -1:
        return (-1, -1)
    else:
        temp = S[top]
        top -= 1
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
    top2 += 1
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
        
        
## Postfix Expression Evaluation using Stack ##

operators = set(['+', '-', '*', '/'])
exp1 = input("Enter Postfix Expression: ")
S = []
top = -1
MAX = 100
for char in exp1:
    if char not in operators:
        top += 1
        S.append(int(char))
    elif char in operators:
        b, top = pop(S, top, MAX)
        a, top = pop(S, top, MAX)
        if char == '+':
            temp = a + b
            top = push(S, temp, top, MAX)
        elif char == '-':
            temp = a - b
            top = push(S, temp, top, MAX)
        elif char == '*':
            temp = a * b
            top = push(S, temp, top, MAX)
        elif char == '/':
            temp = a / b
            top = push(S, temp, top, MAX)
    else:
        print("Invalid Character")
        top = push(S, int(char), top, MAX)
disp(S, top)

def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
    return stack.pop()

print("Postfix Evaluation of '231*+9-':", evaluate_postfix("231*+9-"))  # Output: -4

import re
# ---------- Tokenizer (handles multi-digit and simple unary minus for numbers) ----------
def tokenize(expr):
    '''Tokenize the input expression into numbers, variables, operators and parentheses.
    Handles unary minus for numbers (e.g., -3) but not for variables (e.g., -x).'''
    expr = expr.replace(' ', '')
    # capture floats, ints, names, operators and parentheses
    tokens = re.findall(r'\d+\.\d+|\d+|[A-Za-z]+|[+\-*/^()]', expr)
    # Handle unary minus when it appears before a number or variable:
    res = []
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t == '-' and (i == 0 or tokens[i-1] in '+-*/^('):
            # unary minus: if next token is number, attach sign; if variable or '(', convert to 0 - <expr>
            if i+1 < len(tokens) and re.match(r'\d+(\.\d+)?$', tokens[i+1]):
                res.append('-' + tokens[i+1])
                i += 2
                continue
            else:
                res.append('0')
                res.append('-')
                i += 1
                continue
        res.append(t)
        i += 1
    return res

def is_number(tok):
    '''Check if token is a number (int or float)'''
    return re.match(r'^-?\d+(\.\d+)?$', tok) is not None

def is_operand(tok):
    '''Check if token is an operand (number or variable)'''
    return is_number(tok) or re.match(r'^[A-Za-z]+$', tok) is not None

# 1. Infix to Postfix (Shunting Yard) 
def infix_to_postfix(expr):
    '''Convert infix expression to postfix using Shunting Yard algorithm.
    Supports +, -, *, /, ^ operators and parentheses.
    Handles multi-digit numbers and variables.
    ALGORITHM:
    1. Initialize empty stack for operators and empty list for output.
    2. For each token in the input expression:
        a. If token is an operand (number/variable), add it to output.
        b. If token is '(', push it onto stack.
        c. If token is ')', pop from stack to output until '(' is found.
        d. If token is an operator, pop from stack to output while top of stack has same or greater precedence (considering associativity), then push current operator.
    3. After processing all tokens, pop remaining operators from stack to output.
    4. Return output as a space-separated string.'''
    tokens = tokenize(expr)
    output = []
    stack = []
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    assoc = {'+':'L', '-':'L', '*':'L', '/':'L', '^':'R'}
    # Scan each token in the expression
    for tok in tokens:
        if is_operand(tok):
            output.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Remove '('
            else:
                raise ValueError("Mismatched parentheses")
        else:  # operator
            while (stack and stack[-1] != '(' and
                   ((prec.get(stack[-1],0) > prec.get(tok,0)) or
                    (prec.get(stack[-1],0) == prec.get(tok,0) and assoc.get(tok,'L') == 'L'))):
                output.append(stack.pop())
            stack.append(tok)
    while stack:
        op = stack.pop()
        if op in '()':
            raise ValueError("Mismatched parentheses")
        output.append(op)
    return ' '.join(output)

# 2. Infix to Prefix (via reverse to postfix to reverse) 
def infix_to_prefix(expr):
    '''Convert infix expression to prefix.
    1. Reverse the infix expression.
    2. Swap '(' with ')' and vice versa.
    3. Convert the modified expression to postfix.
    4. Reverse the postfix expression to get prefix.'''
    tokens = tokenize(expr)
    # reverse and swap parens
    rev = []
    for t in tokens[::-1]:
        if t == '(':
            rev.append(')')
        elif t == ')':
            rev.append('(')
        else:
            rev.append(t)
    rev_expr = ''.join(rev)
    post = infix_to_postfix(rev_expr)  # get postfix of reversed expression
    prefix = ' '.join(post.split()[::-1])  # reverse postfix to get prefix
    return prefix

# 3. Evaluate Postfix 
def evaluate_postfix(postfix_expr):
    '''Evaluate a postfix expression.
    Assumes all operands are numbers (int/float).
    ALGORITHM:
    1. Initialize an empty stack.
    2. For each token in the postfix expression:
        a. If token is a number, push it onto the stack.
        b. If token is an operator, pop the top two numbers from the stack, apply the operator, and push the result back onto the stack.
    3. After processing all tokens, the stack should contain one element, which is the result.
    4. Return the result.'''
    tokens = postfix_expr.split()
    stack = []
    for tok in tokens:
        if is_number(tok):
            stack.append(float(tok))
        elif re.match(r'^[A-Za-z]+$', tok):
            raise ValueError("Cannot evaluate variables without values: " + tok)
        else:
            if len(stack) < 2:
                raise ValueError("Malformed expression")
            b = stack.pop()
            a = stack.pop()
            if tok == '+': res = a + b
            elif tok == '-': res = a - b
            elif tok == '*': res = a * b
            elif tok == '/': res = a / b
            elif tok == '^': res = a ** b
            else: raise ValueError("Unknown operator " + tok)
            stack.append(res)
    if len(stack) != 1:
        raise ValueError("Malformed expression after evaluation")
    return stack[0]

# ---------- Evaluate Prefix ----------
def evaluate_prefix(prefix_expr):
    '''Evaluate a prefix expression.
    Assumes all operands are numbers (int/float).
    ALGORITHM:
    1. Initialize an empty stack.
    2. Scan the prefix expression from right to left.
        a. If token is a number, push it onto the stack.
        b. If token is an operator, pop the top two numbers from the stack, apply the operator, and push the result back onto the stack.
    3. After processing all tokens, the stack should contain one element, which is the result.
    4. Return the result.'''
    tokens = prefix_expr.split()[::-1]  # scan right-to-left
    stack = []
    for tok in tokens:
        if is_number(tok):
            stack.append(float(tok))
        elif re.match(r'^[A-Za-z]+$', tok):
            raise ValueError("Cannot evaluate variables without values: " + tok)
        else:
            if len(stack) < 2:
                raise ValueError("Malformed expression")
            a = stack.pop()
            b = stack.pop()
            if tok == '+': res = a + b
            elif tok == '-': res = a - b
            elif tok == '*': res = a * b
            elif tok == '/': res = a / b
            elif tok == '^': res = a ** b
            else: raise ValueError("Unknown operator " + tok)
            stack.append(res)
    if len(stack) != 1:
        raise ValueError("Malformed expression after evaluation")
    return stack[0]

# ---------- Examples ----------
if __name__ == "__main__":
    infix = "5 + ((1 + 2) * 4) - 3"
    postfix = infix_to_postfix(infix)
    prefix = infix_to_prefix(infix)
    print("Infix:  ", infix)
    print("Postfix:", postfix)
    print("Prefix: ", prefix)
    print("Eval Postfix:", evaluate_postfix(postfix))
    print("Eval Prefix: ", evaluate_prefix(prefix))
