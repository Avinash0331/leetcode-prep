class Solution:
    def isValidBST(self, root):
        self.prev = None
        self.ans = True

        def inorder(node):
            if not node or not self.ans: #We already know the tree is invalid → stop everything”
                return
            
            inorder(node.left)
            
            if self.prev is not None and self.prev >= node.val:
                self.ans = False
                return
            
            self.prev = node.val #### Don't forget
            
            inorder(node.right)
        
        inorder(root)
        return self.ans
    
#Example for early stopping
# Tree:
#        5
#       / \
#      1   4
#         / \
#        3   6
#
# Inorder traversal → 1 → 5 → 3 (violation: 3 < 5)
# Once violation found → self.ans = False
# 'if not self.ans' stops further recursion (skips visiting 6)