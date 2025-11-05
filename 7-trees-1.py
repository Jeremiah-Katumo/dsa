class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data
    
    def setData(self, val):
        self.data = val
        
    def display(self):
        print(self.data, end=" ")
        
class BinaryTree1:
    def __init__(self, rootData):
        self.root = Node(rootData)
        self.level = 0
        
    def preorder_traversal(self, root, trav):
        '''Iterative Preorder Traversal
        ALGORITHM:
        1. Create an empty stack S and push root to it.
        2. Do the following while S is not empty.
            a. Pop an item from stack and print it.
            b. Push right child of popped item to S
            c. Push left child of popped item to S
            Note that right child is pushed first so that left is processed first'''
        if root == None:
            return
        else:
            stack_pre = []
            stack_pre.append(root)
            while stack_pre:
                ptr = stack_pre.pop()  # Pop/dequeue the top/front node
                trav.append(ptr.data)  # Process the node
                if ptr:
                    if ptr.left == None and ptr.right == None:
                        print("Leaf Node:", ptr.data)
                        continue
                    if ptr.right != None:  # Push/enqueue right child first so that left is processed first
                        stack_pre.append(ptr.right)
                    if ptr.left != None:
                        stack_pre.append(ptr.left)
                        
    def inorder_traversal(self, root, trav):
        '''Iterative Inorder Traversal
        ALGORITHM:
        1. Create an empty stack S.
        2. Initialize current node as root
        3. Push the current node to S and set current = current->left until current is NULL
        4. If current is NULL and stack is not empty then
            a. Pop the top item from stack.
            b. Print the popped item, set current = popped_item->right
            c. Go to step 3.
        5. If current is NULL and stack is empty then we are done.'''
        if root == None:
            return
        else:
            stack_in = []   # Create an empty stack S.
            ptr = root      # Initialize current node as root
            while stack_in or ptr:
                if ptr != None:
                    stack_in.append(ptr)
                    ptr = ptr.left
                else:
                    ptr = stack_in.pop()
                    trav.append(ptr.data)
                    ptr = ptr.right
                    
    def postorder_traversal(self, root, trav):
        '''Iterative Postorder Traversal
        ALGORITHM:
        1. Create an empty stack S.
        2. Initialize current node as root
        3. Push the current node to S and set current = current->left until current is NULL
        4. If current is NULL and stack is not empty then
            a. Pop the top item from stack.
            b. If the popped item has a right child and the right child is not processed yet then
                i. Push the popped item back to stack.
                ii. Set current = popped_item->right
            c. Else
                i. Print the popped item and set current = NULL
            d. Go to step 3.
        5. If current is NULL and stack is empty then we are done.'''
        if root == None:
            return
        else:
            stack_post = []
            ptr = root
            visited = set()
        
        while stack_post or ptr:
            if ptr:
                stack_post.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack_post.pop()
                if (ptr.right != None) and (ptr.right not in visited):
                    stack_post.append(ptr)
                    ptr = ptr.right
                else:
                    visited.add(ptr)
                    trav.append(ptr.data)
                    ptr = None
                    
    def insertLeft(self, val):
        '''Insert a node as the left child of the root. If the left child 
        already exists, push it down as the left child of the new node.'''
        ptr = self.root
        if ptr.left == None:
            ptr.left = Node(val)
        else:
            temp = Node(val)
            temp.left = ptr.left
            ptr.left = temp
            
    def insertRight(self, val):
        '''Insert a node as the right child of the root. If the right child
        already exists, push it down as the right child of the new node.'''
        ptr = self.root
        if ptr.right == None:
            ptr.right = Node(val)
        else:
            temp = Node(val)
            temp.right = ptr.right
            ptr.right = temp
            
    def insertLevelOrder(self, arr, root, i, n):
        '''Function to insert nodes in level order
        arr: input array
        root: current root of the binary tree
        i: current index in the array
        n: size of the array'''
        if i < n:
            temp = Node(arr[i])
            root = temp
            root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)
            root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root
    
    def deleteLeafNode(self, root, key):
        '''Function to delete a leaf node with a given key
        root: current root of the binary tree
        key: value of the leaf node to be deleted'''
        if root is None:
            return None
        if root.left is None and root.right is None and root.data == key:
            return None
        root.left = self.deleteLeafNode(root.left, key)
        root.right = self.deleteLeafNode(root.right, key)
        return root


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def display(self):
        print(self.key, end=" ")
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, root, key):
        '''Insert a node with the given key into the BST
            root: current root of the BST
            key: value to be inserted
        ALGORITHM:
        1. If the tree is empty, return a new node.
        2. Otherwise, recur down the tree.
        3. Return the (unchanged) node pointer.'''
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        '''Search for a node with the given key in the BST
            root: current root of the BST
            key: value to be searched
        ALGORITHM:
        1. Base Cases: root is null or key is present at root 
        2. Key is greater than root's key so search in right subtree
        3. Key is smaller than root's key so search in left subtree'''
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def delete(self, root, key):
        '''Delete a node with the given key from the BST
            root: current root of the BST
            key: value to be deleted
        ALGORITHM:
        1. If the tree is empty, return root.
        2. Otherwise, recur down the tree.
        3. If the key is the same as root's key, then this is the node to be deleted.
        4. If the key is smaller than root's key, then it lies in left subtree.
        5. If the key is larger than root's key, then it lies in right subtree.
        6. If the node has only one child or no child, then replace the node with its child.
        7. If the node has two children, then find the inorder successor (smallest in the right subtree),
           copy the inorder successor's content to this node and delete the inorder successor.'''
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = self.minValueNode(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)
        return root

    def minValueNode(self, node):
        '''Get the node with the minimum key value found in that tree
            node: current node
        ALGORITHM:
        1. Initialize current as the given node.
        2. Loop down to find the leftmost leaf.'''
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
            
## Implement alternative to Binary Tree Traversal using Recursion and Iteration ##
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Inorder Traversal (Left → Root → Right)
    def inorder_recursive(self, root):
        if root:
            self.inorder_recursive(root.left)
            print(root.key, end=" ")
            self.inorder_recursive(root.right)

    # Preorder Traversal (Root → Left → Right)
    def preorder_recursive(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder_recursive(root.left)
            self.preorder_recursive(root.right)

    # Postorder Traversal (Left → Right → Root)
    def postorder_recursive(self, root):
        if root:
            self.postorder_recursive(root.left)
            self.postorder_recursive(root.right)
            print(root.key, end=" ")

# Iterative Traversals
def inorder_iterative(self, root):
    stack = []
    current = root

    while True:
        # Reach the leftmost node
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.key, end=" ")
            current = current.right
        else:
            break
        
def preorder_iterative(self, root):
    if root is None:
        return
    stack = [root]

    while stack:
        current = stack.pop()
        print(current.key, end=" ")
        # Push right child first so that left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
            
def postorder_iterative(self, root):
    if root is None:
        return
    stack = []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            # If right child exists and traversing node from left child, move to right child
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                print(peek_node.key, end=" ")
                last_visited = stack.pop()
                    
                    
# Define Node and BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return "Tree is empty"
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self.minValueNode(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)
        return root


# --- Example Usage ---
bst = BinarySearchTree()
root = None

# Insert nodes
for key in [50, 30, 20, 40, 70, 60, 80]:
    root = bst.insert(root, key)

print("Inorder Traversal (sorted): ")
bst.inorder(root)  # Output: 20 30 40 50 60 70 80

print("\nPreorder Traversal: ")
bst.preorder(root)  # Output: 50 30 20 40 70 60 80

print("\nPostorder Traversal: ")
bst.postorder(root)  # Output: 20 40 30 60 80 70 50

print("\n\nSearching for 60 →",
      "Found" if bst.search(root, 60) else "Not Found")

root = bst.delete(root, 70)
print("\nAfter deleting 70 (Inorder): ")
bst.inorder(root)  # Output: 20 30 40 50 60 80


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal
    
## Binary Search Tree Implementation with Insert, Search, Delete, and Traversal Methods
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self.minValueNode(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)
        return root