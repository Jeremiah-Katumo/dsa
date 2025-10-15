
def tower_of_hanoi(num, source, dest, aux):
    if num == 1:
        print(f"Move disk 1 from {source} to {dest}")
    else:
        tower_of_hanoi(num - 1, source, aux, dest)  # Move n-1 disks from source to auxiliary
        print(f"Move disk {num} from {source} to {dest}")
        tower_of_hanoi(num - 1, aux, dest, source)  # Move n-1 disks from auxiliary to destination
        
def fibonnacci(n):
    if n <= 1:
        return n
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
    
def fibonnacci(n):
    seq = [0, 1]  # 
    for i in range(n):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

print(fibonnacci(30))

def fibonnaci(n):
    if n <= 1:
        return n
    elif n == 1:
        return n
    elif n == 2:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
    
def even_numbers(num):
    if num % 2 != 0:
        print('Enter an even number')
    elif num == 2:
        return num
    else:
        return even_numbers(num-2)
    
def generate_binary(n):
    if n == 0:
        return ""
    elif n == 1:
        return ['0','1']
    else:
        listt = []
        for i in generate_binary(n-1):
            listt.append('0'+i)
        for i in generate_binary(n-1):
            listt.append('1'+i)
    return listt

def reverse_list(listt):
    if len(listt) == 1:
        return listt
    else:
        return [listt[-1]] + reverse_list(listt[:-1])
    
listt = [4,5,6,7,8]
print(f"Reversed List: {reverse_list(listt)}")

def find_max(listt):
    if len(listt) == 1:
        return listt[0]
    else:
        rest = find_max(listt[1:])
        return listt[0] if listt[0] > rest else rest
    
def reverse_numbers(num):
    if num < 10:
        return str(num)
    else:
        return str(num % 10) + reverse_numbers(num // 10)
    
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1) # recursive
        # fac = 1
        # for i in range(1, n+1):
        #     fac *= i  # iterative
        # return fac