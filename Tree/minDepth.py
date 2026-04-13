def minDepth(root):
    if not root:
        return 0
    left = minDepth(root.left)
    right = minDepth(root.right)
    if not left:
        return right + 1
    if not right:
        return left + 1
    return 1 + min(left,right)

#we have multiple cases for just left or right else the minimum of height, null would always be null.

# Input (Tree):
#        1
#       / 
#      2
#     /
#    3

# Output:
# 3

# Input:
#        1
#       / \
#      2   3

# Output:
# 2