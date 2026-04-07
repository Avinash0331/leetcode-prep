def isSubtree(root,subroot):
    def isSameTree(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    
    if not root:
        return False
    
    if isSameTree(root,subroot):
        return True
    
    return isSubtree(root.left,subroot) or isSubtree(root.right,subroot)

# Input:
# root = [3, 4, 5, 1, 2]
# subroot = [4, 1, 2]

# Tree:
#      3
#     / \
#    4   5
#   / \
#  1   2

# Output:
# True

