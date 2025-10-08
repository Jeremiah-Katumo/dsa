## AVL Tree ##
class AVLNode:
    def __init__(self, key, value=None):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.value = value
        
    def display(self):
        print(self.key, end=" ")
        
class AVLTree:
    def __init__(self):
        self.root = AVLNode(None)
        
    def get_height(self, node):
        return node.height if node else 0
    
    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def get_balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0
    
    def rotate_right(self, y):
        '''Right rotate the subtree rooted with y
            y: root of the subtree to be rotated
        ALGORITHM:
        1. Set x as y's left child.
        2. Set T2 as x's right child.
        3. Perform rotation.
        4. Update heights.
        5. Return new root.'''
        x = y.left
        T2 = x.right
        # Perform rotation
        x.right = y
        y.left = T2
        # Update heights
        self.update_height(y)
        self.update_height(x)
        return x
    
    def rotate_left(self, x):
        '''Left rotate the subtree rooted with x
            x: root of the subtree to be rotated
        ALGORITHM:
        1. Set y as x's right child.
        2. Set T2 as y's left child.
        3. Perform rotation.
        4. Update heights.
        5. Return new root.'''
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y
    
    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)
    
    def _insert(self, node, key, value=None):
        '''Insert a node with the given key and value into the AVL tree
            node: current root of the subtree
            key: value to be inserted
            value: associated value with the key (optional)
        ALGORITHM:
        1. Perform the normal BST insertion.
        2. Update the height of this ancestor node.
        3. Get the balance factor of this ancestor node to check whether this node became unalanced.
        4. If the node becomes unbalanced, then there are 4 cases
            a. Left Left Case
            b. Right Right Case
            c. Left Right Case
            d. Right Left Case'''
        # 1. Perform the normal BST insertion
        if not node or node.key is None:
            return AVLNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # Update value if key already exists
            return node
        # 2. Update the height of this ancestor node
        self.update_height(node)
        # 3. Get the balance factor of this ancestor node to check whether this node became
        balance = self.get_balance_factor(node)
        # 4. If the node becomes unbalanced, then there are 4 cases
        # LL Case
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        # RR Case
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        # LR Case
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # RL Case
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def search(self, key):
        '''Search for a node with the given key in the AVL tree
            key: value to be searched
        ALGORITHM:
        1. Start from the root and traverse the tree.
        2. If the key is found, return the node.
        3. If the key is less than the current node's key, go to the left subtree.
        4. If the key is greater than the current node's key, go to the right subtree.
        5. If the key is not found, return None.'''
        node = self.root
        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
                
        return None
    
    def min_value_node(self, node):
        '''Get the node with the minimum key value found in that tree
            node: current node
        ALGORITHM:
        1. Initialize current as the given node.
        2. Loop down to find the leftmost leaf.'''
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
        
    def _delete(self, node, key):
        '''Delete a node with the given key from the AVL tree
            node: current root of the subtree
            key: value to be deleted
        ALGORITHM:
        1. Perform standard BST delete.
        2. Update the height of the current node.
        3. Get the balance factor of this node (to check whether this node became unbalanced).
        4. If this node becomes unbalanced, then there are 4 cases
            a. Left Left Case
            b. Right Right Case
            c. Left Right Case
            d. Right Left Case'''
        # STEP 1: PERFORM STANDARD BST DELETE
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)
        
        # If the tree had only one node then return
        if not node:
            return node
        
        # STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
        self.update_height(node)
        
        # STEP 3: GET THE BALANCE FACTOR OF THIS NODE (to check whether this node became unbalanced)
        balance = self.get_balance_factor(node)
        
        # STEP 4: IF THIS NODE BECOMES UNBALANCED, THEN THERE ARE 4 CASES
        # LL Case
        if balance > 1 and self.get_balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        # LR Case
        if balance > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # RR Case
        if balance < -1 and self.get_balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        # RL Case
        if balance < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    # traversals
    def inorder(self):
        '''Inorder traversal of the AVL tree
        ALGORITHM:
        1. Traverse the left subtree.
        2. Visit the root.
        3. Traverse the right subtree.'''
        def _inorder(node):
            if node:
                _inorder(node.left)
                node.display()
                _inorder(node.right)
        _inorder(self.root)
        print()
        
    def preorder(self):
        '''Preorder traversal of the AVL tree
        ALGORITHM:
        1. Visit the root.
        2. Traverse the left subtree.
        3. Traverse the right subtree.'''
        def _preorder(node):
            if node:
                node.display()
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        print()
        
    def pretty_print(self, node=None, level=0):
        '''Pretty print the AVL tree
            node: current node (default is root)
            level: current level in the tree (default is 0)
        ALGORITHM:
        1. Recursively print the right subtree.
        2. Print the current node with indentation based on its level.
        3. Recursively print the left subtree.'''
        if node is None:
            node = self.root
        def _pretty_print(node, level):
            if node is not None:
                _pretty_print(node.right, level + 1)
                print(' ' * 4 * level + '->', node.key)
                _pretty_print(node.left, level + 1)
        _pretty_print(node, level)
        
# Example usage
if __name__ == "__main__":
    avl = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        avl.insert(key)
    
    print("Inorder traversal of the constructed AVL tree is:")
    avl.inorder()
    
    print("Preorder traversal of the constructed AVL tree is:")
    avl.preorder()
    
    print("Pretty print of the constructed AVL tree is:")
    avl.pretty_print()
    
    avl.delete(10)
    print("Inorder traversal after deletion of 10:")
    avl.inorder()
    
    avl.delete(20)
    print("Inorder traversal after deletion of 20:")
    avl.inorder()
    
    avl.delete(30)
    print("Inorder traversal after deletion of 30:")
    avl.inorder()
    
    print("Pretty print after deletions:")
    avl.pretty_print()
    
    
## B-Trees ##
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.leaf = leaf  # True if leaf node
        self.keys = []  # List of keys in the node
        self.children = []  # List of child pointers of B-tree node
        
    def display(self):
        print("Keys:", self.keys)
        if not self.leaf:
            for child in self.children:
                child.display()
                
class BTree:
    def __init__(self, t):
        if t < 2:
            raise ValueError("B-Tree minimum degree must be at least 2.")
        self.t = t  # Minimum degree
        self.root = BTreeNode(t, True)  # Create root node
        
    def search(self, node, key):
        '''Search for a key in the B-Tree
            node: current node
            key: value to be searched
        ALGORITHM:
        1. Start from the root and traverse the tree.
        2. Find the first key greater than or equal to the key.
        3. If the found key is equal to the key, return the node.
        4. If the node is a leaf, return None (key not found).
        5. If the node is not a leaf, go to the appropriate child and repeat.'''
        if node is None:
            return None
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node
        if node.leaf:
            return None
        return self.search(node.children[i], key)
        
    def insert(self, key):
        '''Insert a key into the B-Tree
            key: value to be inserted
        ALGORITHM:
        1. If root is full, then tree grows in height.
        2. If root is not full, call insert_non_full for root.'''
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key)
            self.root = new_root
        else:
            self.insert_non_full(root, key)
            
    def insert_non_full(self, node, key):
        '''Insert a key into a non-full node
            node: current node
            key: value to be inserted
        ALGORITHM:
        1. If the node is a leaf, insert the key in the correct position.
        2. If the node is not a leaf, find the child which is going to have the new key.
        3. If the found child is full, split it and then decide which of the two children to recurse to.'''
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)  # Create space for new key
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)
            
    def split_child(self, parent, i):
        '''Split the child of a node
            parent: parent node
            i: index of the child to be split
        ALGORITHM:
        1. Create a new node to store (t-1) keys of y.
        2. Copy the last (t-1) keys of y to z.
        3. If y is not a leaf, copy the last t children of y to z.
        4. Reduce the number of keys in y.
        5. Insert z as a child of parent.
        6. Move the middle key of y up to parent.'''
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)
        
        # Step 1 and 2: Copy the last (t-1) keys of y to z
        z.keys = y.keys[t:(2 * t - 1)]
        mid_key = y.keys[t-1]
        y.keys = y.keys[0:(t - 1)]
        
        # Step 3: If y is not a leaf, copy the last t children of y to z
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]
        
        # Step 4: Reduce the number of keys in y
        # Already done by slicing
        
        # Step 5: Insert z as a child of parent
        parent.children.insert(i + 1, z)
        
        # Step 6: Move the middle key of y up to parent
        parent.keys.insert(i, y.keys.pop())
        
    def delete(self, key):
        '''Delete a key from the B-Tree
            key: value to be deleted
        ALGORITHM:
        1. Start from the root and traverse the tree.
        2. If the key is found in the node and the node is a leaf, remove the key.
        3. If the key is found in the node and the node is not a leaf, replace it with its predecessor or successor and delete that key.
        4. If the key is not found in the node, go to the appropriate child and repeat.
        5. Ensure that the child has at least t keys before descending. If not, fill it by borrowing from a sibling or merging with a sibling.'''
        self._delete(self.root, key)
        if len(self.root.keys) == 0:
            if self.root.leaf:
                self.root = BTreeNode(self.t, True)
            else:
                self.root = self.root.children[0]
                
    def _delete(self, node, key):
        '''Helper function to delete a key from the B-Tree
            node: current node
            key: value to be deleted
        ALGORITHM:
        1. Find the first key greater than or equal to the key.
        2. If the found key is equal to the key, delete it.
        3. If the node is a leaf, return (key not found).
        4. If the node is not a leaf, go to the appropriate child and repeat.
        5. Ensure that the child has at least t keys before descending. If not, 
            fill it by borrowing from a sibling or merging with a sibling.'''
        t = self.t
        idx = 0
        while idx < len(node.keys) and key > node.keys[idx]:
            idx += 1
        
        if idx < len(node.keys) and node.keys[idx] == key:
            if node.leaf:
                node.keys.pop(idx)
            else:
                self._delete_internal_node(node, idx)
        else:
            if node.leaf:
                print("The key", key, "is not present in the tree.")
                return
            flag = (idx == len(node.keys))
            if len(node.children[idx].keys) < t:
                self.fill(node, idx)
            if flag and idx > len(node.keys):
                self._delete(node.children[idx - 1], key)
            else:
                self._delete(node.children[idx], key)
                
    def _delete_internal_node(self, node, idx):
        '''Delete a key from an internal node
            node: current node
            idx: index of the key to be deleted
        ALGORITHM:
        1. If the child that precedes key[idx] has at least t keys,
            find the predecessor 'pred' of key[idx] in the subtree rooted at child[idx].
            Replace key[idx] by pred and recursively delete pred in child[idx].
        2. If the child that follows key[idx] has at least t keys,
            find the successor 'succ' of key[idx] in the subtree rooted at child[idx+1].
            Replace key[idx] by succ and recursively delete succ in child[idx+1].
        3. If both child[idx] and child[idx+1] have only t-1 keys,
            merge key[idx] and all of child[idx+1] into child[idx].
            Now child[idx] contains 2t-1 keys.
            Free child[idx+1] and recursively delete key[idx] from child[idx].'''
        t = self.t
        key = node.keys[idx]
        if len(node.children[idx].keys) >= t:
            pred = self.get_predecessor(node, idx)
            node.keys[idx] = pred
            self._delete(node.children[idx], pred)
        elif len(node.children[idx + 1].keys) >= t:
            succ = self.get_successor(node, idx)
            node.keys[idx] = succ
            self._delete(node.children[idx + 1], succ)
        else:
            self.merge(node, idx)
            self._delete(node.children[idx], key)
            
    def get_predecessor(self, node, idx):
        '''Get the predecessor of a key in the B-Tree
            node: current node
            idx: index of the key
        ALGORITHM:
        1. Move to the rightmost node of the left child of the key.'''
        current = node.children[idx]
        while not current.leaf:
            current = current.children[-1]
        return current.keys[-1]
    
    def get_successor(self, node, idx):
        '''Get the successor of a key in the B-Tree
            node: current node
            idx: index of the key
        ALGORITHM:
        1. Move to the leftmost node of the right child of the key.'''
        current = node.children[idx + 1]
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]
    
    def fill(self, node, idx):
        '''Fill the child node if it has less than t-1 keys
            node: current node
            idx: index of the child to be filled
        ALGORITHM:
        1. If the previous child has more than t-1 keys, borrow a key from that child.
        2. If the next child has more than t-1 keys, borrow a key from that child.
        3. If both children have only t-1 keys, merge the child with one of its siblings.'''
        t = self.t
        if idx != 0 and len(node.children[idx - 1].keys) >= t:
            self.borrow_from_prev(node, idx)
        elif idx != len(node.keys) and len(node.children[idx + 1].keys) >= t:
            self.borrow_from_next(node, idx)
        else:
            if idx != len(node.keys):
                self.merge(node, idx)
            else:
                self.merge(node, idx - 1)
                
    def merge(self, node, idx):
        '''Merge child[idx] with child[idx+1]
            node: current node
            idx: index of the child to be merged
        ALGORITHM:
        1. Move the median key from node to child[idx].
        2. Append keys of child[idx+1] to child[idx].
        3. If child[idx] is not a leaf, append children of child[idx+1] to child[idx].
        4. Remove child[idx+1] from node.'''
        child = node.children[idx]
        sibling = node.children[idx + 1]
        t = self.t
        
        # Step 1: Move the median key from node to child[idx]
        child.keys.append(node.keys[idx])
        
        # Step 2: Append keys of sibling to child
        child.keys.extend(sibling.keys)
        
        # Step 3: If child is not a leaf, append children of sibling to child
        if not child.leaf:
            child.children.extend(sibling.children)
        
        # Step 4: Remove sibling from node
        node.keys.pop(idx)
        node.children.pop(idx + 1)
        
    def borrow_from_prev(self, node, idx):
        '''Borrow a key from the previous sibling
            node: current node
            idx: index of the child to borrow from
        ALGORITHM:
        1. Move a key from node to child[idx].
        2. Move the last key of child[idx-1] to node.
        3. If child[idx] is not a leaf, move the last child of child[idx-1] to child[idx].'''
        child = node.children[idx]
        sibling = node.children[idx - 1]
        
        # Step 1: Moving a key from node to child[idx]
        child.keys.insert(0, node.keys[idx - 1])
        
        # Step 2: Moving the last key of sibling to node
        node.keys[idx - 1] = sibling.keys.pop()
        
        # Step 3: Moving the last child of sibling to child if not leaf
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
            
    def borrow_from_next(self, node, idx):
        '''Borrow a key from the next sibling
            node: current node
            idx: index of the child to borrow from
        ALGORITHM:
        1. Move a key from node to child[idx].
        2. Move the first key of child[idx+1] to node.
        3. If child[idx] is not a leaf, move the first child of child[idx+1] to child[idx].'''
        child = node.children[idx]
        sibling = node.children[idx + 1]
        
        # Step 1: Moving a key from node to child[idx]
        child.keys.append(node.keys[idx])
        
        # Step 2: Moving the first key of sibling to node
        node.keys[idx] = sibling.keys.pop(0)
        
        # Step 3: Moving the first child of sibling to child if not leaf
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
            
    def traverse(self):
        '''Traverse the B-Tree and print all keys
        ALGORITHM:
        1. For each key in the node, print the key and recursively traverse the child before it.
        2. After printing all keys, recursively traverse the last child.'''
        def _traverse(node):
            for i in range(len(node.keys)):
                if not node.leaf:
                    _traverse(node.children[i])
                print(node.keys[i], end=" ")
            if not node.leaf:
                _traverse(node.children[len(node.keys)])
        _traverse(self.root)
        print()
        
# Example usage
if __name__ == '__main__':
    t = 3  # minimum degree
    bt = BTree(t)
    data = [10, 20, 5, 6, 12, 30, 7, 17, 3, 2, 4, 25, 28]
    for x in data:
        bt.insert(x)
    print("Tree after inserts:")
    print(bt.traverse())

    print("Search 17:", bt.search(17) is not None)
    print("Delete 6")
    bt.delete(6)
    print(bt.traverse())
    print("Delete 13 (not present)")
    bt.delete(13)
    print(bt.traverse())
    print("Delete some more keys: 7,4,2,3,5")
    for k in [7,4,2,3,5]:
        bt.delete(k)
    print(bt.traverse())
    