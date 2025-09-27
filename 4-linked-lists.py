
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
                
                
## Cyclic List ##

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