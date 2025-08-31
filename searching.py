class Node:
    def __init__(self, key):
        self.left= None
        self.right= None
        self.key= key
        
class BinarySearchTree:
    def __init__(self):
        self.root= None
        
    #Insert a key
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    #A utility function to search a given key in BST
    def search(self, root, key):
      #Base cases: root is null or key is present at root
      if root is None or root.key == key:
          return root
    
      #Key is greater than root's key
      if key < root.key:
          return self.search(root.left, key)
    
      #Key is smaller than root's key
      return self.search(root.right, key)
  
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end= " ")
            self.inorder(root.right)

bst= BinarySearchTree()
root = None
keys= [50, 30 ,20, 40, 70, 60, 80]

for key in keys:
    root= bst.insert(root, key)
    
print("In-order traversal of the BST: ")
bst.inorder(root)

#Searching for a key
search_key = 40
if bst.search(root, search_key):
    print(f"\nKey {search_key} found in the BST")
else:
    print(f"\nKey {search_key} not found in the BST")