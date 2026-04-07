def findLCABST(root,p,q):
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return findLCABST(root.left,p,q)
    if p.val > root.val and q.val > root.val:
        return findLCABST(root.right,p,q)
    
    return root

# Input (BST):
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5
# p = 2, q = 8

# Output:
# 6

# Input:
# p = 2, q = 4

# Output:
# 2