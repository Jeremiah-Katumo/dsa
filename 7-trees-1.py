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

def delete(self, root, key):
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
        
class BinaryTree1:
    def __init__(self, rootData):
        self.root = Node(rootData)
        self.level = 0
        
    def preorder_traversal(self, root, trav):
        if root == None:
            return
        else:
            stack_pre = []
            stack_pre.append(root)
            while stack_pre:
                ptr = stack_pre.pop()
                trav.append(ptr.data)
                if ptr:
                    if ptr.right != None:
                        stack_pre.append(ptr.right)
                    if ptr.left != None:
                        stack_pre.append(ptr.left)
                        
    def inorder_traversal(self, root, trav):
        if root == None:
            return
        else:
            stack_in = []
            ptr = root
            while stack_in or ptr:
                if ptr != None:
                    stack_in.append(ptr)
                    ptr = ptr.left
                else:
                    ptr = stack_in.pop()
                    trav.append(ptr.data)
                    ptr = ptr.right
                    
    def postorder_traversal(self, root, trav):
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
        ptr = self.root
        if ptr.left == None:
            ptr.left = Node(val)
        else:
            temp = Node(val)
            temp.left = ptr.left
            ptr.left = temp
            
    def insertRight(self, val):
        ptr = self.root
        if ptr.right == None:
            ptr.right = Node(val)
        else:
            temp = Node(val)
            temp.right = ptr.right
            ptr.right = temp
            
    def insertLevelOrder(self, arr, root, i, n):
        if i < n:
            temp = Node(arr[i])
            root = temp
            root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)
            root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root
    
    def deleteLeafNode(self, root, key):
        if root is None:
            return None
        if root.left is None and root.right is None and root.data == key:
            return None
        root.left = self.deleteLeafNode(root.left, key)
        root.right = self.deleteLeafNode(root.right, key)
        return root
                    
                    
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