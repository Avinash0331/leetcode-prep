class Solution:
    def recoverTree(self,root):
        self.g1f = self.g1s = self.g2f = \
        self.g2s = self.prev = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is None:
                self.prev = node #first node, assign root to self.prev
            else:
                if self.prev.val > node.val:
                    #is this the first violation?
                    if self.g1f is None:
                        self.g1f = self.prev
                        self.g1s = node
                    #second violation
                    self.g2f = self.prev
                    self.g2s = node
                self.prev = node #increment the prev variable
            inorder(node.right)
        
        if root is None:
            return
        inorder(root)
        if self.g2f is None: #only 1 violation so swap g1f and g1s
            self.g1f.val,self.g1s.val = self.g1s.val,self.g1f.val
        else:
            self.g1f.val,self.g2s.val = self.g1f.val,self.g2s.val

# Input (BST with swapped nodes):
#        3
#       / \
#      1   4
#         /
#        2

# Output (Recovered BST):
#        2
#       / \
#      1   4
#         /
#        3

# Inorder before fix: 1, 3, 2, 4  (incorrect)
# Inorder after fix:  1, 2, 3, 4  (correct)