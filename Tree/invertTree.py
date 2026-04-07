def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

# Input (Tree):
#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9

# Output (Inverted Tree):
#        4
#       / \
#      7   2
#     / \ / \
#    9  6 3  1