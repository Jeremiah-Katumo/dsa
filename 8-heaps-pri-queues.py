class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        '''Get the index of the parent of the node at index i
            i: index of the node
        ALGORITHM:
        1. Return (i - 1) // 2.'''
        return (i - 1) // 2

    def left(self, i):
        '''Get the index of the left child of the node at index i
            i: index of the node
        ALGORITHM:
        1. Return 2 * i + 1.'''
        return 2 * i + 1

    def right(self, i):
        '''Get the index of the right child of the node at index i
            i: index of the node
        ALGORITHM:
        1. Return 2 * i + 2.'''
        return 2 * i + 2

    def insert(self, val):
        '''Insert a new value into the max heap
            val: value to be inserted
        ALGORITHM:
        1. Add the new value at the end of the heap.
        2. Heapify up from the last index to restore the heap property.'''
        heap = self.heap
        if heap[0] == 0:
            heap[0] == val
        else:
            index = 0
            while heap[index] != 0:
                index += 1
            heap[index] = val
            pos = index
            while pos != 0:
                if (heap[(pos - 1) // 2] < heap[pos]):
                    temp = heap[pos]
                    heap[pos] = heap[(pos - 1) // 2]
                    heap[(pos - 1) // 2] = temp
                    pos = (pos - 1) // 2
                else:
                    break
        # self.heap.append(val)
        # self.heapify_up(len(self.heap) - 1)
        
    def delete(self):
        '''Delete a node from a heap'''
        index = 0
        heap = self.heap
        
        while heap[index] != 0:
            temp = heap[index]
            index1 = index
            index += 1
        if index1 == 0:
            temp1 = heap[0]
            heap[0] = 0
        else:
            temp1 = heap[0]
            heap[0] = temp
            pos = 0
            print(index1)
            
            while pos != index1:
                if (heap[pos] < heap[2 * pos + 1]):
                    heap[pos], heap[2 * pos + 1] = heap[2 * pos + 1], heap[pos]
                    pos = 2 * pos + 1
                    print(pos)
                elif (heap[pos] < heap[2 * pos + 2]):
                    heap[pos], heap[2 * pos + 2] = heap[2 * pos + 2], heap[pos]
                    pos = 2 * pos + 2
                    print(pos)
                    
            return temp1

    def heapify_up(self, i):
        '''Heapify up the value at index i to restore the max heap property
            i: index of the value to be heapified up
        ALGORITHM:
        1. While the current index is not the root and the value at the current index is greater than its parent,
           swap the value with its parent and update the current index to the parent's index.'''
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_max(self):
        '''Extract and return the maximum value from the max heap
        ALGORITHM:
        1. If the heap is empty, return None.
        2. If the heap h as only one element, remove and return it.
        3. Store the root value to be returned later.
        4. Move the last element to the root and remove the last element.
        5. Heapify down from the root to restore the heap property.'''
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        '''Heapify down the value at index i to restore the max heap property
            i: index of the value to be heapified down
        ALGORITHM:
        1. Initialize largest as the current index.
        2. If the left child exists and is greater than the current largest, update largest to the left child's index.
        3. If the right child exists and is greater than the current largest, update largest to the right child's index.
        4. If largest is not the current index, swap the values and recursively heapify down from the largest index.'''
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)
