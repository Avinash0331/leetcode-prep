def flipTree(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val!=root2.val:
        return False
    
    flip = flipTree(root1.left,root2.right) and flipTree(root1.right, root2.left)
    no_flip = flipTree(root1.left,root2.left) and flipTree(root1.right,root2.right)
    return flip or no_flip

# Input:
# Tree 1:          Tree 2:
#     1                1
#    / \              / \
#   2   3            3   2
#  /                  \
# 4                    4

# Output:
# True

# Input:
# Tree 1:          Tree 2:
#     1                1
#    / \              / \
#   2   3            2   4

# Output:
# False