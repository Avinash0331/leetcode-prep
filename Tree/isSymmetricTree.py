def isSymmetric(root):
    
    def isMirror(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return isSymmetric(p.left,q.right) and isSymmetric(p.right,q.left)
    return isMirror(root.left,root.right)

# Input (Symmetric Tree):
#        1
#       / \
#      2   2
#     / \ / \
#    3  4 4  3

# Output:
# True


# Input (Not Symmetric):
#        1
#       / \
#      2   2
#       \   \
#        3    3

# Output:
# False