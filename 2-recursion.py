import sys
import time

## 1. Tower of Hanoi ##

def TowerOfHanoi(num, source, destination, auxilliary):
    if num == 1:
        print("Move disk 1 from", source, 'to', destination)
        return
    else:
        TowerOfHanoi(num-1, source, destination, auxilliary)
        print(f"Move disk {num} from {source} to {destination}")
        TowerOfHanoi(num-1, source, destination, auxilliary)

TowerOfHanoi(4, 'A', 'C', 'B')

## 2. Rabbit Problem (Fibonnacci) ##

# Iterative Approach
def Fibonacci(n):
    seq = [0,1]
    for i in range(n):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

tic = time.time()
Fibonacci(30)
toc = time.time()
elapsed = toc - tic
print(f"Iterative Approach: {elapsed}")
    
# Recursive Approach
def fibonacci(n):
    if n <= 1:
        return n
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
tic = time.time()
fibonacci(30)
toc = time.time()
elapsed = toc - tic
print(f"Recursive Approach: {elapsed}")


def EvenNumbers(num):
    print(num)
    if num % 2 != 0:
        print("Please enter an even number")
    elif num == 2:
        return num
    else:
        return EvenNumbers(num-2)
    
print(f"Even numbers: {EvenNumbers(10)}")

## 3. Generating Binary Numbers ##
def generate(n):
    if n == 0:
        return ""
    elif n == 1:
        return ['0','1']
    else:
        listt = []
        for i in generate(n-1):
            listt.append('0'+i)
        for i in generate(n-1):
            listt.append('1'+i)
    return listt        

print(f"Binary Numbers Generated: {generate(5)}")

## 4. Lists ##
def reverse(listt):
    if (len(listt) == 1):
        return listt
    else:
        return [listt[-1]] + reverse(listt[:-1])
    
listt = [4,5,6,7,8]
print(f"Reversed List: {reverse(listt)}")

def find_max(listt):
    if (len(listt) == 1):
        return listt[0]
    else:
        rest = find_max(listt[1:])
        return listt[0] if listt[0] > rest else rest
    
print(f"Maximum Number: {find_max(listt)}")

## Reverse Numbers ##
def digits(num):
    digit = 1
    while num // 10 != 0:
        digit += 1
        num = num // 10
    return digit

def rev_number(num):
    if (num // 10 == 0):
        return num
    else:
        digit = digits(rev_number(num // 10))
        num1 = (num % 10) * (10**digit) + rev_number(num // 10)
        return num1
    
print(f"Reversed Number: {rev_number(12345)}")

tic = time.time()
rev_number(12345)
toc = time.time()
elapsed = toc - tic
print(f"Recursive Approach: {elapsed}")

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        rev = (rev * 10) + (n % 10)
        return reverse_number(n // 10, rev)
    
print(f"Reversed Number: {reverse_number(12345)}")

tic = time.time()
reverse_number(12345)
toc = time.time()
elapsed = toc - tic
print(f"Recursive Approach: {elapsed}")


## Iterative Approach of Factorial
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac

## Recursive Approach of Factorial
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    

# sum of first n natural numbers using recursion   
def sum_natural(n):
    # Base case
    if n == 0:
        return 0
    # Recursive case
    return n + sum_natural(n - 1)

# Example usage
n = 10
print("Sum of first", n, "natural numbers is:", sum_natural(n))


# Find the first n terms of the Fibonacci series using recursion.
def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_series(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
    
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive step
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_series(n):
    series = []
    for i in range(n):
        series.append(fibonacci(i))
    return series

# Example usage
n = 10
print("First", n, "terms of Fibonacci series:", fibonacci_series(n))


def find_max(listt):
    if (len(listt) == 1):
        return listt[0]
    else:
        rest = find_max(listt[1:])
        return listt[0] if listt[0] > rest else rest
    
def find_min(listt):
    if (len(listt) == 1):
        return listt[0]
    else:
        rest = find_min(listt[1:])
        return listt[0] if listt[0] < rest else rest

def find_sum(listt):
    if (len(listt) == 1):
        return listt[0]
    else:
        return listt[0] + find_sum(listt[1:])
    
# Palindrome Check
def palindrome_check(val: str | int):
    if isinstance(val, int):
        val = str(val)
    if len(val) <= 1:
        return True
    else:
        if val[0] != val[-1]:
            return False
        else:
            return palindrome_check(val[1:-1])
        
print(f"Palindrome Check: {palindrome_check('madam')}")
print(f"Palindrome Check: {palindrome_check('hello')}")
print(f"Palindrome Check: {palindrome_check(121)}")
print(f"Palindrome Check: {palindrome_check(123)}")


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 2)
    
print(f"Sum of Digits: {sum_of_digits(12345)}")

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        rev = (rev * 10) + (n % 10)
        return reverse_number(n // 10, rev)
    
print(f"Reversed Number: {reverse_number(12345)}")

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
print(f"GCD: {gcd(48, 18)}")

def min_sum_list(L, n):
    if n == 0:
        return 0
    else:
        return L[n-1] + min_sum_list(L, n-1)
    
L = [3,5,2,8,1]
n = len(L)
print(f"Sum of List: {min_sum_list(L, n)}")

def Min_sum_list(listt):
    return min(listt, key=lambda x: x if x > 0 else sys.maxsize)

print(f"Minimum Positive Number: {Min_sum_list([-1, -3, 4, 2, 0, -5, 6])}")


def Generate_binary(n, prefix=''):
    if n == 0:
        return [prefix]
    else:
        return Generate_binary(n-1, prefix + '0') + Generate_binary(n-1, prefix + '1')
    
print(f"Binary Numbers Generated: {Generate_binary(3)}")

def Generate_hex(n, prefix=""):
    hex_digits = "0123456789ABCDEF"

    # Base case
    if len(prefix) == n:
        print(prefix)
        return

    # Recursive case: try each hex digit
    for digit in hex_digits:
        return Generate_hex(n, prefix + digit)
       
print(f"Hexadecimal Numbers Generated: {Generate_hex(2)}") 

def generate_hex(n, prefix=''):
    if n == 0:
        return [prefix]
    else:
        hex_chars = '0123456789ABCDEF'
        result = []
        for char in hex_chars:
            result.extend(generate_hex(n-1, prefix + char))
        return result
    
print(f"Hexadecimal Numbers Generated: {generate_hex(2)}")

def generate_permutations(s):
    if len(s) == 0:
        return ['']
    else:
        perms = []
        for i, char in enumerate(s):
            for perm in generate_permutations(s[:i] + s[i+1:]):
                perms.append(char + perm)
        return perms    
    
print(f"Permutations Generated: {generate_permutations('ABC')}")
