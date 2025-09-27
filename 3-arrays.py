import numpy as np
import time
import random

## Insertion and Deletion ##

max = 50

def insert_beginning(arr, n, item):
    if n != max:
        i = n - 1
        while (i >= 0 and arr[i] > item):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = item
        insert_beginning(arr, n + 1, item)
        
def insert_beg(arr, n, item):
    if n != max:
        i = n - 1
        while (i > 0):
            arr[i + 1] = arr[i]
            i -= 1
        arr[0] = item
        n += 1
    else:
        print('Overflow')
        
        
def insert_end(arr, n, item):
    if n != max:
        arr[n] = item
        n += 1
    else:
        print('Overflow')
        
        
def delete_beg(arr, n):
    if n != 0:
        i = 0
        while (i <= (n - 1)):
            arr[i - 1] = arr[i]
            i += 1
        n -= 1
    else:
        print('Underflow')
        
        
def delete_after(arr, n, item):
    if n != 0:
        i = 0
        while (i <= (n - 1) and arr[i] != item):
            i += 1
        if i < n - 1:
            while (i <= (n - 1)):
                arr[i] = arr[i + 1]
                i += 1
            n -= 1
        else:
            print('Item not found or no element after it')
    else:
        print('Underflow')
        
        
def del_after(arr, n, val):
    if(val):
        i=n-1
            
        while(arr[i] != val):
            i-=1
        i+=1
        while(i>n-1):
            arr[i]= arr[i+1]
            i+=1
        n-=1
    else:
        print('Not Found')
        
        
def delete_end(arr, n):
    if n != 0:
        arr[n - 1] = 0
        n -= 1
    else:
        print('Underflow')
        
        
max_size = 100

def insert_beginning(arr, item):
    if len(arr) >= max_size:
        print('Overflow')
        return arr
    return [item] + arr

def insert_end(arr, item):
    if len(arr) >= max_size:
        print('Overflow')
        return arr
    arr.append(item)
    return arr

def delete_beg(arr):
    if not arr:
        print('Underflow')
        return arr
    return arr[1:]

def delete_end(arr):
    if not arr:
        print('Underflow')
        return arr
    arr.pop()
    return arr

def delete_after(arr, item):
    if not arr:
        print('Underflow')
        return arr
    try:
        idx = arr.index(item)
        if idx < len(arr) - 1:
            del arr[idx + 1]
        else:
            print('Item not found or no element after it')
    except ValueError:
        print('Item not found')
    return arr



class Array:
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.arr = [0]*max
        
    def insert_beg(self, item):
        if (self.n != self.max):
            i = self.n - 1
            while (i > 0):
                self.arr[i + 1] = self.arr[i]
                i -= 1
            self.arr[i + 1] = item
            self.n += 1
        else:
            print('Overflow')
            
    def insert_after(self, val, item):
        if (self.n != self.max):
            i = self.n - 1
            while (self.arr[i] != val):
                self.arr[i + 1] = self.arr[i]
                i -= 1
            self.arr[i + 1] = item
            self.n += 1
        else: 
            print('Overflow')
            
    def insert_end(self, item):
        if (self.n != self.max):
            self.arr[self.n] = item
            self.n += 1
        else:
            print('Overflow')
            
    def del_beg(self):
        if (self.n != 0):
            i = 1
            while (i <= self.n - 1):
                self.arr[i - 1] = self.arr[i]
                i += 1
            self.n -= 1
        else:
            print('Underflow')
            
    def del_after(self, val):
        if (val in self.arr):
            i = self.n - 1
            while (self.arr[i] != val):
                i -= 1
            i += 1
            while (i < self.n - 1):
                self.arr[i] = self.arr[i + 1]
                i += 1
            self.n -= 1
        else:
            print('Underflow')
            
    def del_end(self):
        if (self.n != 0):
            self.n -= 1
        else:
            print('Underflow')
            
    def display(self):
        print('Array\t: ', self.arr[:self.n])
        
        
## Linear Search ##

def find_max(arr, n):
    max1 = 0
    for i in range(1, n):
        if arr[i] > max1:
            max1 = arr[i]
    return max1

def Find_max(listt):
    if (len(listt) == 1):
        return listt[0]
    else:
        rest = find_max(listt[:1])
        return listt[0] if listt[0] > rest else rest

def find_min(arr, n):
    min1 = 0
    for i in range(1, n):
        if arr[i] < min1:
            min1 = arr[i]
    return min1

def Find_min(listt):
    if (len(listt) == 1):
        return listt[0]
    else:
        rest = find_max(listt[:1])
        return listt[0] if listt[0] < rest else rest
    
def recursive_sum(arr, n):
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]
    return sum1

def Recursive_sum(listt):
    if not listt:
        return 0
    else:
        return listt[0] + Recursive_sum(listt[1:])
    
tic = time.time()
listt = [4,5,6,7,8]
Recursive_sum(listt)
toc = time.time()
elapsed = toc - tic
print(f"Recursive Approach: {elapsed}")

tic = time.time()
recursive_sum(listt, len(listt))
toc = time.time()
elapsed = toc - tic
print(f"Iterative Approach: {elapsed}")


def find_product(arr, n):
    prod1 = 1
    for i in range(n):
        prod1 *= arr[1]
    return prod1

def linear_search(arr, n, item):
    for i in range(n):
        if arr[i] == item:
            return i
    # return -1

def Linear_search(listt, item):
    if (len(listt) == 0):
        return -1
    elif (listt[0] == item):
        return 0
    else:
        idx = Linear_search(listt[1:], item)
        return idx + 1 if idx != -1 else -1
    
def linear_search(arr, n, item):
    indices = []
    for i in range(n):
        if arr[i] == item:
            indices.append(i)
    return indices

def linear_search_all(listt, n, item):
    flag = 0
    for i in range(n):
        if listt[i] == item:
            print(f"Item found at index {i}")
            flag = 1
    if flag == 0:
        print("Item not found")
        
def count_occurrences(arr, n, item):
    count = 0
    for i in range(n):
        if arr[i] == item:
            count += 1
    return count

def find_mean(arr, n):
    sum1 = recursive_sum(arr, n)
    mean1 = sum1 / n
    return mean1

def Find_mean(listt):
    if (len(listt) == 1):
        return listt[0]
    else:
        return (listt[0] + Find_mean(listt[1:]) * (len(listt) - 1)) / len(listt)
    
def find_median(arr, n):
    arr.sort()
    if n % 2 == 0:
        median1 = (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        median1 = arr[n // 2]
    return median1

def Find_median(listt):
    listt.sort()
    if len(listt) % 2 == 0:
        median1 = listt[len(listt) // 2 - 1] + listt[len(listt) // 2] / 2
    else:
        median1 = listt[len(listt) // 2]
    return median1

def find_mode(arr, n):
    freq = {}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    mode1 = max(freq, key=freq.get)
    return mode1

def Find_mode(listt):
    freq = {}
    for i in range(len(listt)):
        if listt[i] in freq:
            freq[listt[i]] += 1
        else:
            freq[listt[i]] = 1
    mode1 = max(freq, key=freq.get)
    return mode1

def find_quartiles(arr, n):
    arr.sort()
    Q2 = find_median(arr, n)
    if n % 2 == 0:
        lower_half = arr[:n // 2]
        upper_half = arr[n // 2:]
    else:
        lower_half = arr[:n // 2]
        upper_half = arr[n // 2 + 1:]
    Q1 = find_median(lower_half, len(lower_half))
    Q3 = find_median(upper_half, len(upper_half))
    return Q1, Q2, Q3

def Find_quartiles(listt):
    listt.sort()
    Q2 = Find_median(listt)
    if len(listt) % 2 == 0:
        lower_half = listt[:len(listt) // 2]
        upper_half = listt[len(listt) // 2:]
    else:
        lower_half = listt[:len(listt) // 2]
        upper_half = listt[len(listt) // 2 + 1:]
    Q1 = Find_median(lower_half)
    Q3 = Find_median(upper_half)
    return Q1, Q2, Q3

def Find_Quartile(arr, n):
    arr1 = sorted(arr)
    print(arr1)
    return arr1[(n + 1) // 4], arr1[(n + 1) // 2], arr1[(3 * n) // 4]

def find_quar_devition(arr, n):
    Q1, Q2, Q3 = find_quartiles(arr, n)
    QD = (Q3 - Q1) / 2
    return QD


## Problems on Recursion ##
def cluster_odds_and_evens(arr, n):
    left, right = 0, n - 1
    while left < right:
        while arr[left] % 2 == 1 and left < right:
            left += 1
        while arr[right] % 2 == 0 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr

print(f"Clustered Odds and Evens: {cluster_odds_and_evens([12, 3, 5, 8, 7, 10, 19, 4], 8)}")

def Cluster_odds_and_evens(listt):
    left, right = 0, len(listt) - 1
    while left < right:
        while listt[left] % 2 == 1 and left < right:
            left += 1
        while listt[right] % 2 == 0 and left < right:
            right -= 1
        if left < right:
            listt[left], listt[right] = listt[right], listt[left]
            left += 1
            right -= 1
            
    return listt

print(f"Clustered Odds and Evens: {Cluster_odds_and_evens([12, 3, 5, 8, 7, 10, 19, 4])}")


def cluster_odds_evens(arr):
    arr1 = np.zeros(arr.shape[0], dtype=int)  # new array of same size
    k = 0
    
    # Step 1: collect odds
    for i in range(arr.shape[0]):
        if arr[i] % 2 != 0:
            arr1[k] = arr[i]
            k += 1

    # Step 2: collect evens
    for i in range(arr.shape[0]):
        if arr[i] % 2 == 0:
            arr1[k] = arr[i]
            k += 1

    return arr1


# Example usage
arr = np.array([12, 3, 5, 8, 7, 10, 1, 6])
print("Original array:", arr)
print("Clustered array:", cluster_odds_evens(arr))


def cluster_positives_and_negatives(arr, n):
    left, right = 0, n - 1
    while left < right:
        while arr[left] >= 0 and left < right:
            left += 1
        while arr[right] <= 0 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    return arr

arr = [3, -2, 5, -8, 7, -1, 4, -6]
print("Partitioned array:", cluster_positives_and_negatives(arr, 8))

def Cluster_positives_and_negatives(listt):
    left, right = 0, len(listt) - 1
    while left < right:
        while listt[left] >= 0 and left < right:
            left += 1
        while listt[right] <= 0 and left < right:
            right -= 1
        if left < right:
            listt[left], listt[right] = listt[right], listt[left]
            left += 1
            right -= 1
    
    return listt

arr = [3, -2, 5, -8, 7, -1, 4, -6]
print("Clustered Positives and Negatives:", Cluster_positives_and_negatives(arr))


def stable_partition_pos_neg(arr):  # Preserving order (stable, O(n) with extra array)
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    return pos + neg

# Example
arr = [3, -2, 5, -8, 7, -1, 4, -6]
print("Stable partitioned array:", stable_partition_pos_neg(arr))


def find_pairs_bruteforce(arr, val):
    pairs = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == val:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1, 5, 7, -1, 5]
val = 6
print("Pairs:", find_pairs_bruteforce(arr, val))


def find_pairs_hashing(arr, val):
    pairs = []
    seen = set()
    for num in arr:
        target = val - num
        if target in seen:
            pairs.append((target, num))
        seen.add(num)
    return pairs

arr = [1, 5, 7, -1, 5]
val = 6
print("Pairs using hashing:", find_pairs_hashing(arr, val))


def find_pairs_two_pointer(arr, target):
    arr.sort()  # sort in non-decreasing order
    left, right = 0, len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs


# Example usage
arr = [1, 5, 7, -1, 5, 2, 4, 3]
target = 6
print("Pairs:", find_pairs_two_pointer(arr, target))


def elements_greater_than_mean(arr):
    mean_val = sum(arr) / len(arr)
    return [x for x in arr if x > mean_val]

# Example
arr = [10, 20, 30, 40, 50]
print("Elements greater than mean:", elements_greater_than_mean(arr))


def indices_above_99_percentile(marks):
    cutoff = np.percentile(marks, 99)   # 99th percentile value
    return [i for i, m in enumerate(marks) if m > cutoff]

# Example
marks = [random.randint(0, 100) for _ in range(1000)]
print("Indices of students > 99th percentile:", indices_above_99_percentile(marks))


def indices_below_1_percentile(marks):
    cutoff = np.percentile(marks, 1)   # 1st percentile value
    return [i for i, m in enumerate(marks) if m < cutoff]

print("Indices of students < 1st percentile:", indices_below_1_percentile(marks))


def Repeated_elements(arr):
    seen = set()
    repeated = set()
    n = len(arr)
    for i in range(n):
        if arr[i] in seen:
            repeated.add(arr[i])
        else:
            seen.add(arr[i])
    return list(repeated)

print(f"Repeated Elements: {Repeated_elements([1,2,3,2,4,5,6,2,4,3,7,8,9])}")

def repeated_elements(arr):
    flag = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j] and i != j:
                flag += 1
                print(f"Number of Repeated Elements: {flag}")
    return flag

print(f"Repeated Elements: {repeated_elements([1,2,3,2,4,5,6,2,4,3,7,8,9])}")


def frequency_count(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

def frequency_count(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

print(f"Frequency Count: {frequency_count([1,2,3,2,4,5,6,2,4,3,7,8,9])}")


def frequency_count_sorted(arr):
    arr.sort()
    freq = {}
    counts = 1
    n = len(arr)
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            counts += 1
        else:
            freq[arr[i - 1]] = counts
            counts = 1
    freq[arr[n - 1]] = counts  # for the last element
    return freq

print(f"Frequency Count Sorted: {frequency_count_sorted([1,2,3,2,4,5,6,2,4,3,7,8,9])}")

def sort_by_frequency(arr):
    freq = frequency_count(arr)
    # Sort by frequency (value) and then by number (key)
    sorted_items = sorted(freq.items(), key=lambda x: (x[1], x[0]))
    sorted_arr = []
    for num, count in sorted_items:
        sorted_arr.extend([num] * count)
    return sorted_items

print(f"Sorted by Frequency: {sort_by_frequency([1,2,3,2,4,5,6,2,4,3,7,8,9])}")
    
    
def find_missing_sum(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(f"Missing sum: {find_missing_sum([1,2,3,5], 5)}")

def find_missing_xor(arr, n):
    xor_all = 0
    for i in range(1, n+1):
        xor_all ^= i
    xor_arr = 0
    for num in arr:
        xor_arr ^= num
    return xor_all ^ xor_arr

print(find_missing_xor([1,2,3,5], 5))  # Missing 4

def find_missing_hash(arr, n):
    seen = set(arr)
    for i in range(1, n+1):
        if i not in seen:
            return i

print(find_missing_hash([1,2,3,5], 5))  # Missing 4
