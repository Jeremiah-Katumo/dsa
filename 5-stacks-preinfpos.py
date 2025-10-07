class Stack:
    """Simple stack implementation"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


class ExpressionConverter:
    """Convert between infix, prefix, and postfix notations"""
    def __init__(self):
        # Define operator precedence
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.right_associative = {'^'}
    
    def is_operator(self, char):
        return char in self.precedence
    
    def is_operand(self, char):
        return char.isalnum()
    
    # INFIX TO POSTFIX
    def infix_to_postfix(self, expression):
        """Convert infix expression to postfix using stack"""
        stack = Stack()
        postfix = []
        # Scan each character in the expression
        for char in expression:
            if char.isspace():
                continue
            
            if self.is_operand(char):
                postfix.append(char)            
            elif char == '(':
                stack.push(char)            
            elif char == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove '('            
            elif self.is_operator(char):  # Operator
                while (not stack.is_empty() and stack.peek() != '(' and
                        stack.peek() in self.precedence and
                        ((self.precedence[stack.peek()] > self.precedence[char]) or
                        (self.precedence[stack.peek()] == self.precedence[char] and 
                        char not in self.right_associative))):
                    postfix.append(stack.pop())
                stack.push(char)
        while not stack.is_empty():
            if stack.peek() == '(':
                stack.pop()
            if stack.pop() in '()':
                raise ValueError("Mismatched parentheses")
            postfix.append(stack.pop())
        
        return ''.join(postfix)
    
    # INFIX TO PREFIX
    def infix_to_prefix(self, expression):
        """Convert infix expression to prefix using stack"""
        # Reverse the expression
        reversed_exp = expression[::-1]
        # Replace ( with ) and vice versa
        temp = []
        for char in reversed_exp:
            if char == '(':
                temp.append(')')
            elif char == ')':
                temp.append('(')
            else:
                temp.append(char)
        
        reversed_exp = ''.join(temp)
        # Get postfix of modified expression
        postfix = self.infix_to_postfix(reversed_exp)
        # Reverse postfix to get prefix
        return postfix[::-1]
    
    # POSTFIX TO INFIX
    def postfix_to_infix(self, expression):
        """Convert postfix expression to infix using stack"""
        stack = Stack()
        
        for char in expression:
            if char.isspace():
                continue
            
            if self.is_operand(char):
                stack.push(char)
            elif self.is_operator(char):
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = f"({operand1}{char}{operand2})"
                stack.push(result)
        
        return stack.pop()
    
    # PREFIX TO INFIX
    def prefix_to_infix(self, expression):
        """Convert prefix expression to infix using stack"""
        stack = Stack()
        
        # Read expression from right to left
        for char in reversed(expression):
            if char.isspace():
                continue
            
            if self.is_operand(char):
                stack.push(char)
            
            elif self.is_operator(char):
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = f"({operand1}{char}{operand2})"
                stack.push(result)
        
        return stack.pop()
    
    # POSTFIX TO PREFIX
    def postfix_to_prefix(self, expression):
        """Convert postfix to prefix using stack"""
        stack = Stack()
        
        for char in expression:
            if char.isspace():
                continue
            
            if self.is_operand(char):
                stack.push(char)
            
            elif self.is_operator(char):
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = char + operand1 + operand2
                stack.push(result)
        
        return stack.pop()
    
    # PREFIX TO POSTFIX
    def prefix_to_postfix(self, expression):
        """Convert prefix to postfix using stack"""
        stack = Stack()
        
        # Read expression from right to left
        for char in reversed(expression):
            if char.isspace():
                continue
            
            if self.is_operand(char):
                stack.push(char)
            
            elif self.is_operator(char):
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = operand1 + operand2 + char
                stack.push(result)
        
        return stack.pop()


class ExpressionEvaluator:
    """Evaluate expressions in different notations"""
    
    def evaluate_postfix(self, expression):
        """Evaluate postfix expression"""
        stack = Stack()
        
        for char in expression.split():
            if char.isdigit() or (char[0] == '-' and len(char) > 1):
                stack.push(int(char))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.apply_operator(operand1, operand2, char)
                stack.push(result)
        
        return stack.pop()
    
    def evaluate_prefix(self, expression):
        """Evaluate prefix expression"""
        stack = Stack()
        
        # Read from right to left
        tokens = expression.split()
        for char in reversed(tokens):
            if char.isdigit() or (char[0] == '-' and len(char) > 1):
                stack.push(int(char))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = self.apply_operator(operand1, operand2, char)
                stack.push(result)
        
        return stack.pop()
    
    def apply_operator(self, op1, op2, operator):
        """Apply arithmetic operation"""
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return op1 // op2  # Integer division
        elif operator == '^':
            return op1 ** op2
        return 0


# DEMONSTRATION
if __name__ == "__main__":
    converter = ExpressionConverter()
    evaluator = ExpressionEvaluator()
    
    print("=" * 60)
    print("EXPRESSION NOTATION CONVERTER & EVALUATOR")
    print("=" * 60)
    
    # Example 1: Conversions
    infix = "A+B*C"
    print(f"\n1. INFIX EXPRESSION: {infix}")
    print(f"   Postfix: {converter.infix_to_postfix(infix)}")
    print(f"   Prefix: {converter.infix_to_prefix(infix)}")
    
    # Example 2: Complex expression with parentheses
    infix2 = "(A+B)*C-D"
    print(f"\n2. INFIX EXPRESSION: {infix2}")
    print(f"   Postfix: {converter.infix_to_postfix(infix2)}")
    print(f"   Prefix: {converter.infix_to_prefix(infix2)}")
    
    # Example 3: Postfix to other notations
    postfix = "ABC*+"
    print(f"\n3. POSTFIX EXPRESSION: {postfix}")
    print(f"   Infix: {converter.postfix_to_infix(postfix)}")
    print(f"   Prefix: {converter.postfix_to_prefix(postfix)}")
    
    # Example 4: Prefix to other notations
    prefix = "*+ABC"
    print(f"\n4. PREFIX EXPRESSION: {prefix}")
    print(f"   Infix: {converter.prefix_to_infix(prefix)}")
    print(f"   Postfix: {converter.prefix_to_postfix(prefix)}")
    
    # Example 5: Evaluation with numbers
    print(f"\n5. EVALUATION EXAMPLES:")
    postfix_eval = "2 3 + 4 *"
    prefix_eval = "* + 2 3 4"
    print(f"   Postfix '{postfix_eval}' = {evaluator.evaluate_postfix(postfix_eval)}")
    print(f"   Prefix '{prefix_eval}' = {evaluator.evaluate_prefix(prefix_eval)}")
    
    # Example 6: More complex evaluation
    postfix_complex = "5 6 2 + * 12 4 / -"
    print(f"   Postfix '{postfix_complex}' = {evaluator.evaluate_postfix(postfix_complex)}")
    print(f"   (This is: 5 * (6 + 2) - 12 / 4 = 5 * 8 - 3 = 37)")
    
    print("\n" + "=" * 60)