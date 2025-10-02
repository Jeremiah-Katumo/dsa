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
    return re.match(r'^-?\d+(\.\d+)?$', tok) is not None

def is_operand(tok):
    return is_number(tok) or re.match(r'^[A-Za-z]+$', tok) is not None

# ---------- Infix -> Postfix (Shunting Yard) ----------
def infix_to_postfix(expr):
    tokens = tokenize(expr)
    output = []
    stack = []
    prec = {'+':1, '-':1, '*':2, '/':2, '^':3}
    assoc = {'+':'L', '-':'L', '*':'L', '/':'L', '^':'R'}

    for tok in tokens:
        if is_operand(tok):
            output.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
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

# ---------- Infix -> Prefix (via reverse -> postfix -> reverse) ----------
def infix_to_prefix(expr):
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
    rev_expr = ' '.join(rev)
    post = infix_to_postfix(rev_expr)
    prefix = ' '.join(post.split()[::-1])
    return prefix

# ---------- Evaluate Postfix ----------
def evaluate_postfix(postfix_expr):
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
